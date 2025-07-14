import streamlit as st
import google.generativeai as genai
from utils.gemini_fallback import get_valid_response
# Load all API keys from secrets.toml
API_KEYS = st.secrets["GEMINI_KEYS"]

# Main function to answer question based on document
def answer_question(document_text, user_question):
    prompt = f"""You are a helpful assistant. Based only on the document below, answer the question accurately and justify it with a paragraph reference if possible.

Document:
\"\"\"{document_text}\"\"\"

Question:
{user_question}

Answer (include justification):
"""
    return get_valid_response(prompt)
