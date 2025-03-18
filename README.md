# Prompt Optimizer

An open-source tool for optimizing prompts for AI models.

## Features

- Customize prompts based on tone, length, format, and more
- Support for multiple open-source AI models
- Lightweight and easy to self-host
- No external API keys required
- Generate multiple variants of optimized prompts

## Requirements

- Python 3.8+
- 8GB RAM minimum (more for larger models)
- GPU recommended but not required

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/prompt-optimizer.git
cd prompt-optimizer
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Download a model (optional, will be downloaded automatically on first run):

```bash
python models/download_model.py --model EleutherAI/gpt-neo-125M
```

## Usage

1. Start the application:

```bash
python app.py
```

2. Open your browser and navigate to # Prompt Optimizer

An open-source tool for optimizing prompts for AI models.

## Features

- Customize prompts based on tone, length, format, and more
- Support for multiple open-source AI models
- Lightweight and easy to self-host
- No external API keys required
- Generate multiple variants of optimized prompts

## Requirements

- Python 3.8+
- 8GB RAM minimum (more for larger models)
- GPU recommended but not required

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/prompt-optimizer.git
cd prompt-optimizer
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Download a model (optional, will be downloaded automatically on first run):

```bash
python models/download_model.py --model EleutherAI/gpt-neo-125M
```

## Usage

1. Start the application:

```bash
python app.py
```

2. Open your browser and navigate to http://127.0.0.1:5001

3. Enter your prompt and select your preferred customization options

4. Click "Optimize Prompt" to generate optimized versions of your prompt

## Available Models

The application supports several open-source models from Hugging Face:

- GPT-Neo (125M) - Lightweight, fast, good for basic optimization
- GPT-Neo (1.3B) - Better quality but requires more resources
- BLOOM (560M) - Multilingual capabilities
- OPT (350M) - Good balance of speed and quality

## Adding Custom Models

To add support for additional models:

1. Edit the `get_models()` function in `app.py` to include your model
2. Make sure the model is compatible with Hugging Face's Transformers library
3. Pre-download the model using the `download_model.py` script

## Tips for Best Results

- Start with clear, concise prompts
- Be specific about what you want from the AI model
- Experiment with different tones and formats
- Adjust the character limit based on your needs

## Troubleshooting

- **Out of memory errors**: Try using a smaller model or reduce the number of variants
- **Slow generation**: Consider using a GPU or a smaller model
- **Model loading errors**: Check your internet connection and try running the download script manually

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

3. Enter your prompt and select your preferred customization options

4. Click "Optimize Prompt" to generate optimized versions of your prompt

## Available Models

The application supports several open-source models from Hugging Face:

- GPT-Neo (125M) - Lightweight, fast, good for basic optimization
- GPT-Neo (1.3B) - Better quality but requires more resources
- BLOOM (560M) - Multilingual capabilities
- OPT (350M) - Good balance of speed and quality

## Adding Custom Models

To add support for additional models:

1. Edit the `get_models()` function in `app.py` to include your model
2. Make sure the model is compatible with Hugging Face's Transformers library
3. Pre-download the model using the `download_model.py` script

## Tips for Best Results

- Start with clear, concise prompts
- Be specific about what you want from the AI model
- Experiment with different tones and formats
- Adjust the character limit based on your needs

## Troubleshooting

- **Out of memory errors**: Try using a smaller model or reduce the number of variants
- **Slow generation**: Consider using a GPU or a smaller model
- **Model loading errors**: Check your internet connection and try running the download script manually

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
