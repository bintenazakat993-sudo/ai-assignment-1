import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

# Load model
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit UI
st.title("AI Study Assistant")

st.write("Ask questions about studies and programming")

question = st.text_input("Enter your question:")

if st.button("Submit"):

    if question:

        try:
            response = model.generate_content(question)

            st.subheader("AI Response:")
            st.write(response.text)

        except Exception as e:
            st.error(f"Error: {e}")
    st.write(response.text)
