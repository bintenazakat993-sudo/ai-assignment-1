import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("AI Study Assistant")

st.write("Ask questions about studies and programming")

question = st.text_input("Enter your question:")

if st.button("Submit"):

    system_prompt = """
    You are a friendly study assistant.
    Explain concepts simply for beginners.
    """

    final_prompt = system_prompt + question

    response = model.generate_content(final_prompt)

    st.subheader("AI Response:")

    st.write(response.text) 
