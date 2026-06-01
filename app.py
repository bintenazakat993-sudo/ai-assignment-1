import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API key safely
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ GEMINI_API_KEY .env file mein nahi mili!")
    st.stop()

# Remove any extra spaces
api_key = api_key.strip()

genai.configure(api_key=api_key)

# Correct Model
model = genai.GenerativeModel("gemini-1.5-flash")

st.title("AI Study Assistant")
st.write("Ask questions about studies and programming")

question = st.text_input("Enter your question:")

if st.button("Submit"):
    if not question:
        st.warning("Please enter a question!")
    else:
        with st.spinner("AI soch raha hai..."):
            try:
                system_prompt = """
                You are a friendly study assistant.
                Explain concepts simply for beginners.
                """

                final_prompt = system_prompt + "\n\nQuestion: " + question

                response = model.generate_content(final_prompt)
                
                st.subheader("AI Response:")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
