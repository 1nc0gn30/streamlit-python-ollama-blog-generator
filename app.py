import streamlit as st
import subprocess
import json
import os
from datetime import datetime

BLOGS_FILE = "blogs.json"

# Load previous blogs from file (or create file if it doesn't exist)
def load_blogs():
    if os.path.exists(BLOGS_FILE):
        with open(BLOGS_FILE, "r") as f:
            return json.load(f)
    return []

# Save blogs to file
def save_blogs(blogs):
    with open(BLOGS_FILE, "w") as f:
        json.dump(blogs, f, indent=4)

# Pull a model from Ollama CLI
def pull_model(model_name):
    result = subprocess.run(
        ["ollama", "pull", model_name], capture_output=True, text=True
    )
    if result.returncode != 0:
        st.error(f"Error pulling model: {result.stderr}")
    else:
        st.success(f"Model '{model_name}' pulled successfully!")

# List available models from Ollama
def list_models():
    result = subprocess.run(
        ["ollama", "list"], capture_output=True, text=True
    )
    if result.returncode != 0:
        st.error(f"Error listing models: {result.stderr}")
        return []
    return [line.split()[0] for line in result.stdout.strip().splitlines()]

# Generate a blog using the selected model with `ollama run`
def generate_blog(model, topic):
    prompt = (
        f"Write a detailed, SEO-optimized blog on '{topic}'. "
        "Make it professional, engaging, and filled with relevant keywords."
    )

    # Use `ollama run` to interact with the model
    result = subprocess.run(
        ["ollama", "run", model], input=prompt, text=True, capture_output=True
    )

    if result.returncode != 0:
        st.error(f"Error generating blog: {result.stderr}")
        return None

    return result.stdout.strip()

# Streamlit App
st.title("Neal Frazier's Blog Generator with Ollama")

# Sidebar: Model Selection
st.sidebar.header("Model Management")
available_models = list_models()
model_name = st.sidebar.selectbox("Select a model", available_models)

new_model = st.sidebar.text_input("New model to pull (e.g., 'nealscoder')")
if st.sidebar.button("Pull Model"):
    if new_model:
        pull_model(new_model)
        st.experimental_rerun()  # Refresh to show new model

# Topic Selection for the Blog
st.subheader("Generate a Blog")
topics = [
    "Web Development",
    "App Development",
    "Programming Languages",
    "Libraries & Frameworks",
    "Pentesting & Cybersecurity",
    "Latest Cybersecurity News",
]
topic = st.selectbox("Select a topic", topics)

# Button to generate a new blog
if st.button("Generate Blog"):
    with st.spinner("Generating your blog..."):
        blog_content = generate_blog(model_name, topic)
        if blog_content:
            new_blog = {
                "topic": topic,
                "model": model_name,
                "content": blog_content,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
            blogs = load_blogs()
            blogs.append(new_blog)
            save_blogs(blogs)
            st.success("New blog generated!")
            st.subheader(new_blog["topic"])
            st.write(new_blog["content"])

# Sidebar: View All Generated Blogs
st.sidebar.header("All Generated Blogs")
blogs = load_blogs()
if blogs:
    for i, blog in enumerate(blogs):
        with st.sidebar.expander(f"{i + 1}. {blog['topic']} - {blog['timestamp']}"):
            st.write(blog["content"])
else:
    st.sidebar.write("No blogs generated yet.")

