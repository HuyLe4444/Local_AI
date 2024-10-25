# Product Review Web Scraper

A Python-based web scraper designed to collect product reviews from websites. This tool allows you to input multiple URLs and automatically extracts review content, saving it to a formatted output file.

## Features

- Bulk scraping of product reviews from multiple URLs
- Clean output formatting with reviews numbered and separated
- Browser simulation to reduce blocking probability
- Simple file-based input/output system

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Requirements](#requirements)
- [Project Structure](#project-structure)

---

## Installation

Before running the script, you need to set up a Python environment with the required dependencies.

### Using Conda

1. First, create a new conda environment using the provided `requirement.yaml` file:

   \`\`\`bash
   conda env create -f requirement.yaml
   \`\`\`

2. Activate the environment:

   \`\`\`bash
   conda activate review-comment-scraper
   \`\`\`

---

## Usage

1. **Place your URLs in a text file**: Create a text file (`input.txt`) with each URLs on a new line.

   Example:

   \`\`\`
   https://www.bestbuy.com/site/samsung-galaxy-ring-size-before-you-buy-size-5-titanium-gold/6588067.p?skuId=6588067

   https://www.bestbuy.com/site/eufy-security-solocam-s220-2-indoor-outdoor-wireless-2k-solar-powered-security-cameras-with-16gb-homebase-3-white/6584161.p?skuId=6584161
   \`\`\`

2. **Run the Python script**

3. **Check the output**: The generated reviews will be saved in the `output.txt` file.
---

## Requirements

To run the project, the following dependencies are required, which are listed in the `requirement.yaml` file:


## Project Structure

\`\`\`
├── question.txt            # Input file containing the prompts
├── answer2.txt             # Output file where the model's responses will be saved
├── requirements.yaml       # Conda environment dependencies file
├── response_generator.py   # Main Python script for generating AI responses
└── README.md               # Project documentation (this file)
\`\`\`

---

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute this project as long as proper attribution is provided.

---

## Author 
Huy Le Cong Khanh
-  hule@siue.edu
-  800759103
