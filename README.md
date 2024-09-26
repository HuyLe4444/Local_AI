
# AI Response Generator

This project utilizes the Hugging Face `transformers` library and PyTorch to generate AI responses to text prompts using a pre-trained causal language model (`GPT-Neo`). The script reads prompts from a text file, generates responses for each prompt, and saves the generated text to an output file.

## Features

- Uses the `GPT-Neo` model to generate human-like text responses.
- Supports advanced text generation techniques like **top-k sampling**, **nucleus (top-p) sampling**, and **temperature control**.
- Simple interface for reading prompts from a file and writing generated responses back to a file.
- Extensible and can be easily adapted to other transformer models.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [How it Works](#how-it-works)
- [Requirements](#requirements)
- [Project Structure](#project-structure)

---

## Installation

Before running the script, you need to set up a Python environment with the required dependencies.

### Using Conda

1. First, create a new conda environment using the provided `requirement.yaml` file:

   \`\`\`bash
   conda env create -f requirements.yaml
   \`\`\`

2. Activate the environment:

   \`\`\`bash
   conda activate ai-response-generator
   \`\`\`

---

## Usage

1. **Place your prompts in a text file**: Create a text file (`question.txt`) with each prompt on a new line.

   Example:

   \`\`\`
   What is your name?
   Who trained you?
   Am I your friend? please do not say no, I really like you?
   \`\`\`

2. **Run the Python script**

3. **Check the output**: The generated responses will be saved in the `answer2.txt` file. Each response will be separated by two blank lines for readability.

---

## How it Works

1. **Model Selection**: The script uses the Hugging Face `AutoModelForCausalLM` and `AutoTokenizer` classes to load the pre-trained `GPT-Neo` model from the Hugging Face model hub.

2. **Prompt Tokenization**: The script reads prompts from a text file and uses the tokenizer to convert the text into tokens that the model can process.

3. **Response Generation**: The model generates text based on the prompt using parameters like:
   - `max_length`: The maximum number of tokens the model can generate.
   - `repetition_penalty`: Penalizes repeated words to encourage diversity.
   - `top_k`: Limits the number of tokens to sample from for each word generation.
   - `top_p`: Implements nucleus sampling for controlling randomness.
   - `temperature`: Adjusts the model’s creativity by controlling the probability distribution of the next word.

4. **Decoding and Output**: The generated token sequences are decoded back into text, and the responses are written to an output file.

---

## Requirements

To run the project, the following dependencies are required, which are listed in the `requirements.yaml` file:

### Conda Dependencies:

- **Python** (version 3.10.13)
- **PyTorch** (version 2.4.0)
- **Transformers** (latest version from the `conda-forge` channel)
- **Tqdm** (for progress bars)
- **Tokenizers** (for efficient tokenization)
- **CPU-Only** support (does not require GPU but can be extended for CUDA usage)

### Pip Dependencies:

- **aiohttp** (version 3.8.6)
- **requests** (for making HTTP requests)

---

## Project Structure

\`\`\`
├── question.txt            # Input file containing the prompts
├── answer2.txt             # Output file where the model's responses will be saved
├── requirements.yaml       # Conda environment dependencies file
├── response_generator.py   # Main Python script for generating AI responses
└── README.md               # Project documentation (this file)
\`\`\`

---

## Customization

- **Model**: You can easily switch the model by changing the `model_name` variable in the script. For example, you can use `gpt-neo-1.3B` or any other model available on Hugging Face.
- **Prompt Length**: Modify the `max_length` argument in the `generate` function to control how much text is generated.
- **Sampling Parameters**: Adjust parameters such as `top_k`, `top_p`, and `temperature` to fine-tune the creativity and randomness of the generated text.

---

## Troubleshooting

- **Slow Response Generation**: If you find the generation slow, it's because the model is running on the CPU (`cpuonly`). You can speed it up by running the script on a machine with a GPU. Modify the script to include GPU support by enabling CUDA in PyTorch:
  
  \`\`\`python
  device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
  \`\`\`

- **Memory Issues**: If you encounter memory issues, try using a smaller model or reducing the `max_length` of generated tokens.

---

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute this project as long as proper attribution is provided.

---

## Acknowledgments

- **Hugging Face** for providing the `transformers` library and pre-trained models.
- **PyTorch** for the deep learning framework.

---

