import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("models/gemini-1.5-flash-latest")


def answer_question(document_text, user_question):
    prompt = f"""You are a helpful assistant. Based only on the document below, answer the question accurately and justify it with a paragraph reference if possible.

Document:
{document_text}

Question:
{user_question}

Answer (include justification):
"""
    response = model.generate_content(prompt)
    return response.text.strip()
