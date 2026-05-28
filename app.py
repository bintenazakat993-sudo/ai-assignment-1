import streamlit as st
import google.generativeai as genai
import os

# Get API key from Streamlit secrets
api_key = st.secrets["GEMINI_API_KEY"]

# Configure Gemini
genai.configure(api_key=api_key)

# Load model
model = genai.GenerativeModel("gemini-1.5-flash")

# UI
st.title("AI Study Assistant")
st.write("Ask questions about studies and programming")

question = st.text_input("Enter your question:")

if st.button("Submit"):

    if question:

        system_prompt = """
        You are a friendly study assistant.
        Explain concepts simply for beginners.
        """

        final_prompt = system_prompt + question

        try:
            response = model.generate_content(final_prompt)

            st.subheader("AI Response:")
            st.write(response.text)

        except Exception as e:
            st.error(f"Error: {e}")
    st.write(response.text)
