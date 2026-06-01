import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("XAI_API_KEY")

if not api_key:
    st.error("❌ XAI_API_KEY .env file mein nahi mili!")
    st.stop()

client = OpenAI(
    api_key=api_key,
    base_url="https://api.x.ai/v1"
)

st.title("🧠 Grok AI Study Assistant")
st.write("Koi bhi sawal poochho - Studies, Programming, ML, Assignment etc.")

question = st.text_input("Enter your question:")

if st.button("Submit"):
    if not question:
        st.warning("Question likho!")
    else:
        with st.spinner("Grok jawab de raha hai..."):
            try:
                response = client.chat.completions.create(
                    model="grok-3",
                    messages=[
                        {"role": "system", "content": "You are a helpful study assistant. Explain in easy language, mix Urdu if needed."},
                        {"role": "user", "content": question}
                    ],
                    temperature=0.7,
                    max_tokens=1200
                )
                st.subheader("Grok Response:")
                st.write(response.choices[0].message.content)
            except Exception as e:
                st.error(f"Error: {str(e)}")
