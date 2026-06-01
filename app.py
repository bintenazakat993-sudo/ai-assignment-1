import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY").strip()  # .strip() added for safety

if not api_key:
    st.error("API Key nahi mili .env file mein!")
    st.stop()

genai.configure(api_key=api_key)

# Fixed Model Name
model = genai.GenerativeModel("gemini-1.5-flash")

st.title("AI Study Assistant")
st.write("Ask questions about studies and programming")

question = st.text_input("Enter your question:")

if st.button("Submit"):
    if question:
        with st.spinner("Thinking..."):
            system_prompt = """
            You are a friendly study assistant.
            Explain concepts simply for beginners.
            """
            
            final_prompt = system_prompt + "\n\nQuestion: " + question
            
            try:
                response = model.generate_content(final_prompt)
                st.subheader("AI Response:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter a question!")
