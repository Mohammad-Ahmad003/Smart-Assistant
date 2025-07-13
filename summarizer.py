import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("models/gemini-1.5-flash-latest")



def generate_summary(text):
    prompt = f"Summarize the following document in 150 words or fewer:\n\n{text}"
    response = model.generate_content(prompt)
    return response.text
