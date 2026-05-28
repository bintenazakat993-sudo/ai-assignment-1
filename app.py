import streamlit as st
import google.generativeai as genai

# Load API key from Streamlit Secrets
api_key = st.secrets["GEMINI_API_KEY"]

# Configure Gemini
genai.configure(api_key=api_key)

# Load model
model = genai.GenerativeModel("gemini-1.5-flash")

# App title
st.title("AI Study Assistant")

st.write("Ask questions about studies and programming")

# User input
question = st.text_input("Enter your question:")

# Button click
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

    else:
        st.warning("Please enter a question.")
