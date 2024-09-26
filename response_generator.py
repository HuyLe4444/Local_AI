# File: cs.py
# Description: This script reads prompts from a text file, generates responses using a pre-trained language model (GPT-Neo),
#              and writes the generated responses into an output file.

# Import Libraries
# import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

def read_prompts(file_path):
    """
    Read prompts from a text file.
    Args:
    - file_path (str): The path to the file containing the prompts.
    Return:
    - list of prompts
    """
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def write_responses(file_path, responses):
    """
    Write responses to a text file.
    Args:
    - file_path (str): The path to the file where the responses will be written.
    - responses (list of str): The list of generated responses.
    Return: 
    - none
    """
    with open(file_path, 'w') as file:
        for response in responses:
            file.write(response + '\n\n')

def generate_responses(prompt, model_name):
    """
    Generate responses using the model.
    Args:
    - prompt (str): The input prompt for the model.
    - model_name (str): The name of the pre-trained model from Hugging Face.
    Returns:
    - the generated response for the given prompt.  
    """
    
    # Load the tokenizer and model from Hugging Face's model hub
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    # Tokenize the prompt input and convert it into tensors
    inputs = tokenizer(prompt, return_tensors="pt")
    
    # Generate a response with specified parameters for more controlled text generation
    outputs = model.generate(
        **inputs,
        max_length=100,          # Limit the length of the output
        repetition_penalty=2.0,  # Penalize repeating tokens
        no_repeat_ngram_size=3,  # Prevent repetition of any 3-gram sequences
        top_k=50,                # Limit sampling to top 50 tokens
        top_p=0.95,              # Nucleus sampling, controlling randomness 
        temperature=0.7          # Adjusts creativity in generation
    )
    
    # Decode the generated output tokens back into a human-readable string
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return response

def main():
    # Define model name and check if CUDA is available
    model_name = "EleutherAI/gpt-neo-125M"
    # device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # File paths
    input_file = "question.txt"
    output_file = "answer2.txt"

    # Step 1: Read prompts from the input file
    prompts = read_prompts(input_file)

    # Step 2: Generate responses for each prompt
    responses = []
    
    # For each prompt, generate a response and store it in the list
    for prompt in prompts:
        response = generate_responses(prompt, model_name)
        responses.append(response)
        # print(prompt)

    # Step 3: Write the responses to the output file
    write_responses(output_file, responses)

    print(f"Responses have been written to {output_file}")

# Entry point
if __name__ == "__main__":
    main()
