from flask import Flask, render_template, request, jsonify
import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import gc

app = Flask(__name__)

# Global variables for model and tokenizer
model = None
tokenizer = None
text_generator = None

def load_model(model_name="EleutherAI/gpt-neo-125M"):
    """Load model and tokenizer from Hugging Face"""
    global model, tokenizer, text_generator
    
    print(f"Loading model: {model_name}")
    
    # Free up memory if model was previously loaded
    if model is not None:
        del model
        del tokenizer
        del text_generator
        torch.cuda.empty_cache() if torch.cuda.is_available() else None
        gc.collect()
    
    # Load model and tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        low_cpu_mem_usage=True
    )
    
    # Move model to GPU if available
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = model.to(device)
    
    # Create text generator
    text_generator = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        device=0 if torch.cuda.is_available() else -1
    )
    
    print(f"Model loaded on {device}")

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/api/models')
def get_models():
    """Return available models"""
    models = [
        {"id": "EleutherAI/gpt-neo-125M", "name": "GPT-Neo (125M)"},
        {"id": "EleutherAI/gpt-neo-1.3B", "name": "GPT-Neo (1.3B)"},
        {"id": "bigscience/bloom-560m", "name": "BLOOM (560M)"},
        {"id": "facebook/opt-350m", "name": "OPT (350M)"}
    ]
    return jsonify(models)

@app.route('/api/optimize-prompt', methods=['POST'])
def optimize_prompt():
    """Optimize the user's prompt based on parameters"""
    data = request.json
    
    # Extract parameters
    raw_prompt = data.get('prompt', '')
    tone = data.get('tone', 'neutral')
    length = data.get('length', 'medium')
    format_type = data.get('format', 'paragraph')
    model_name = data.get('model', 'EleutherAI/gpt-neo-125M')
    role = data.get('role', 'general')
    char_limit = data.get('charLimit', 500)
    variants = data.get('variants', 1)
    
    # Check if we need to load a different model
    global model, tokenizer, text_generator
    if model is None or model_name != getattr(model, '_name_or_path', ''):
        load_model(model_name)
    
    # Create optimization instruction based on parameters
    instruction = f"""
    Optimize this prompt: "{raw_prompt}"
    
    Make it:
    - Tone: {tone}
    - Length: {length}
    - Format: {format_type}
    - Writing as a: {role}
    - Character limit: {char_limit}
    
    Optimized prompt:
    """
    
    # Generate optimized prompts
    results = []
    
    try:
        for _ in range(min(variants, 3)):  # Limit to max 3 variants
            outputs = text_generator(
                instruction,
                max_length=len(instruction.split()) + char_limit//4,  # Approximate words from char limit
                num_return_sequences=1,
                temperature=0.7,
                top_p=0.9,
                do_sample=True
            )
            
            generated_text = outputs[0]['generated_text']
            
            # Extract only the generated part (after "Optimized prompt:")
            try:
                optimized_prompt = generated_text.split("Optimized prompt:")[1].strip()
            except IndexError:
                optimized_prompt = generated_text.replace(instruction, "").strip()
            
            # Apply character limit
            if len(optimized_prompt) > char_limit:
                optimized_prompt = optimized_prompt[:char_limit]
            
            results.append(optimized_prompt)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    return jsonify({"results": results})

@app.route('/api/change-model', methods=['POST'])
def change_model():
    """Change the active model"""
    data = request.json
    model_name = data.get('model', 'EleutherAI/gpt-neo-125M')
    
    try:
        load_model(model_name)
        return jsonify({"success": True, "model": model_name})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Load default model on startup
    load_model()
    app.run(debug=True, port=5001)
