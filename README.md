Data Science Advance Project
# Chatbot Development

A lightweight, fully local AI chatbot built using Python, Streamlit, and Ollama. This project runs offline on your machine using the Phi3 Mini model (or any Ollama-supported model).

## Features
- Runs 100% locally (no API keys or internet required)
- Uses Ollama for efficient local inference
- Clean Streamlit web interface
- Easily replaceable model (e.g., llama3.2:1b, mistral, gemma)

## Prerequisites
- Python 3.9+
- 16 GB RAM or higher
- Ollama installed (https://ollama.com/download)

## Setup

```bash
# Clone your project (optional)
git clone https://github.com/your-username/chatbot-development.git
cd chatbot-development

# Create a virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows
# source venv/bin/activate   # On Mac/Linux

# Install dependencies
pip install streamlit requests

# Install and run Ollama
# Download Ollama from https://ollama.com/download
# Then pull the Phi3 Mini model
ollama pull phi3:mini

# Start the Ollama server (keep it running)
ollama serve

# Run the Chatbot (CLI)
python chatbot.py

# Run the Streamlit Web App
streamlit run app.py

# Then open your browser at:
http://localhost:8501
```

## File Structure
Chatbot Development/
├── chatbot.py      # Command-line chatbot
├── app.py          # Streamlit web app
├── venv/           # Virtual environment
└── README.md       # Documentation

## To run Ollama on CPU, set this before starting:
```
set OLLAMA_NUM_GPU=0  # Windows
export OLLAMA_NUM_GPU=0  # Mac/Linux
```

## Contributing
Contributions are welcome!
Feel free to fork the repository, improve the game, and open a pull request. Let's grow this classic game together!

## License
This project is licensed under the [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)

## Author
**Aarya Mehta**  
🔗 [GitHub Profile](https://github.com/AaryaMehta2506)


