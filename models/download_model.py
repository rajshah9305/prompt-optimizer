#!/usr/bin/env python3
"""
Script to download and prepare models for the Prompt Optimizer tool.
This allows users to pre-download models for offline use.
"""

import os
import argparse
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def download_model(model_name, save_path=None):
    """
    Download a model and tokenizer from Hugging Face Hub
    
    Args:
        model_name (str): Name of the model on Hugging Face
        save_path (str, optional): Path to save the model. Defaults to None.
    """
    print(f"Downloading model: {model_name}")
    
    # Create directory if save_path is provided
    if save_path:
        os.makedirs(save_path, exist_ok=True)
        target_path = os.path.join(save_path, model_name.split('/')[-1])
        print(f"Model will be saved to: {target_path}")
    else:
        # Will use the default cache location
        target_path = None
    
    # Download tokenizer
    print("Downloading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    # Download model
    print("Downloading model (this may take a while)...")
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        low_cpu_mem_usage=True
    )
    
    # Save to specified path if provided
    if target_path:
        print(f"Saving model to {target_path}...")
        model.save_pretrained(target_path)
        tokenizer.save_pretrained(target_path)
    
    print(f"Successfully downloaded {model_name}")
    return True

def main():
    parser = argparse.ArgumentParser(description="Download models for Prompt Optimizer")
    parser.add_argument("--model", type=str, default="EleutherAI/gpt-neo-125M", 
                        help="Model name on Hugging Face Hub")
    parser.add_argument("--save-path", type=str, default=None,
                        help="Path to save the model (optional)")
    
    args = parser.parse_args()
    download_model(args.model, args.save_path)

if __name__ == "__main__":
    main()