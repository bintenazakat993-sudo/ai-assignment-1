import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

# Load model
model = genai.GenerativeModel("gemini-2.5-flash")

# App title
st.title("AI Study Assistant")

st.write("Ask questions about studies, programming, or concepts.")

# User input
user_question = st.text_input("Enter your question:")

# Button
if st.button("Submit"):

    system_prompt = """
    You are a friendly study assistant.
    Explain topics in simple language for beginners.
    Give short and clear answers.
    """

    final_prompt = system_prompt + user_question

    response = model.generate_content(final_prompt)

    st.subheader("AI Response:")

    st.write(response.text)
