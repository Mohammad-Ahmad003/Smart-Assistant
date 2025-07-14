
import streamlit as st
import google.generativeai as genai
from utils.gemini_fallback import get_valid_response

# Load multiple Gemini API keys from secrets
API_KEYS = st.secrets["GEMINI_KEYS"]

# Main summary function
def generate_summary(text):
    prompt = f"Summarize the following document in 150 words or fewer:\n\n{text}"
    return get_valid_response(prompt)
