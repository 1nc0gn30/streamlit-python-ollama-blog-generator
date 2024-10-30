# Neal Frazier's Blog Generator with Ollama

This application is a Streamlit-based tool designed to generate SEO-optimized blogs using models from the Ollama CLI. 

## Features
- Generate professional, SEO-rich content on various topics.
- Manage and pull models using the Ollama CLI.
- Store and view all generated blogs within the application.

## Prerequisites
Before running the application, ensure the following prerequisites are met:
- **Python 3.8+**
- **Ollama CLI** installed on your system.
- Streamlit installed (`pip install streamlit`).

## Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/1nc0gn30/streamlit-python-ollama-blog-generator
   cd https://github.com/1nc0gn30/streamlit-python-ollama-blog-generator

2. Install dependencies:

pip install -r requirements.txt


3. Ensure the Ollama CLI is installed and authenticated: You can follow Ollama’s setup instructions for details.



Usage

1. Run the Streamlit app:

streamlit run app.py


2. Generate a blog:

Select a model from the sidebar or pull a new one using the provided text input.

Choose a topic and click Generate Blog.

View the generated blog and its content directly in the main app window.



3. Manage Models:

Use the sidebar to pull new models and list available ones from the Ollama CLI.




File Structure

app.py: Main Streamlit application.

blogs.json: Stores all generated blogs.

requirements.txt: List of required Python packages.


Troubleshooting

If you encounter errors related to the Ollama CLI, ensure it is correctly installed and accessible via the command line.

For missing dependencies, try re-running the pip install -r requirements.txt command.
