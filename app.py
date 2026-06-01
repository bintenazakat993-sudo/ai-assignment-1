import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("XAI_API_KEY")

if not api_key:
    st.error("XAI_API_KEY .env mein nahi mili!")
    st.stop()

client = OpenAI(
    api_key=api_key.strip(),   # extra spaces remove karta hai
    base_url="https://api.x.ai/v1"
)

st.title("🧠 Grok AI Study Assistant")
st.write("Koi bhi sawal poochho!")

question = st.text_input("Enter your question:")

if st.button("Submit"):
    if question:
        with st.spinner("Grok soch raha hai..."):
            try:
                response = client.chat.completions.create(
                    model="grok-3",
                    messages=[
                        {"role": "system", "content": "You are a friendly study assistant."},
                        {"role": "user", "content": question}
                    ]
                )
                st.subheader("Grok Response:")
                st.write(response.choices[0].message.content)
            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.warning("Question likho!")
