import streamlit as st
import google.generativeai as genai

# Load all API keys from secrets.toml
API_KEYS = st.secrets["GEMINI_KEYS"]

# Function to get answer using available keys
def get_valid_response(prompt):
    for key in API_KEYS:
        try:
            genai.configure(api_key=key)
            model = genai.GenerativeModel("models/gemini-1.5-flash-latest")
            response = model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            print(f"Key failed: {key[:6]}... | Reason: {str(e)}")
            continue
    return "❌ All API keys failed or quota exceeded. Please try again later."

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
