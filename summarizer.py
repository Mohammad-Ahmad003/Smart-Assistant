
import streamlit as st
import google.generativeai as genai

# Load multiple Gemini API keys from secrets
API_KEYS = st.secrets["GEMINI_KEYS"]

# Function to get response using first working key
def get_valid_summary(prompt):
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

# Main summary function
def generate_summary(text):
    prompt = f"Summarize the following document in 150 words or fewer:\n\n{text}"
    return get_valid_summary(prompt)
