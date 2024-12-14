import logging
import sys
import os
import time
import streamlit as st
from llama_index.core import Settings, VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.gemini import GeminiEmbedding
import google.generativeai as genai
# import json
# from datetime import datetime

# Configure logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

# Configure API key
GOOGLE_API_KEY = "your_api_key"  # Replace with your actual Google API key
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize Gemini LLM and embedding model
llm = Gemini(
    api_key=GOOGLE_API_KEY,
    # temperature=0.7
    temperature=0.3,  # Precise responses for business context
    max_tokens=512  # Long responses when necessary
)

embed_model = GeminiEmbedding(
    api_key=GOOGLE_API_KEY
)

# Configure settings using the new approach
Settings.llm = llm
Settings.embed_model = embed_model
# Settings.chunk_size = 1024
# Settings.chunk_overlap = 20
Settings.chunk_size = 512  # Smaller chunks for better context handling
Settings.chunk_overlap = 50  # Overlap to maintain context between chunks

# Load documents
file_path = "C:/Users/reda/Downloads/Hackathon_Smartdoc.ai-main/MappedTexts/MappedTexts.txt"
if not os.path.exists(file_path):
    raise FileNotFoundError(f"File not found at {file_path}")

reader = SimpleDirectoryReader(input_files=[file_path])
documents = reader.load_data()

# Create vector index using the configured settings
vector_index = VectorStoreIndex.from_documents(documents)

# Initialize chat engine
chat_engine = vector_index.as_chat_engine(similarity_top_k=5)

# # Create centered main title
st.title('Chat with SFCR Docs')

def response_generator(prompt):
    response = chat_engine.query(prompt)
    print(type(response))
    for word in str(response).split():
        yield word + " "
        time.sleep(0.05)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Ask me anything!"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator(prompt))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content":response})