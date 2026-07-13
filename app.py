import streamlit as st
from groq import Groq
from dotenv import load_dotenv
from reportlab.pdfgen import canvas
import tempfile
import os

# =========================
# Load Environment
# =========================
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

# =========================
# Page Config
# =========================
st.set_page_config(
    page_title="Student Mentor AI",
    page_icon="🎓",
    layout="wide"
)

# =========================
# Custom CSS
# =========================
st.markdown("""
<style>

body{
background-color:#F5F7FA;
}

.main{
background:#F5F7FA;
}

h1{
color:#1E3A8A;
text-align:center;
font-weight:bold;
}

h3{
color:#2563EB;
}

.stButton>button{
background:#2563EB;
color:white;
border:none;
border-radius:12px;
padding:10px;
font-size:17px;
font-weight:bold;
width:100%;
}

.stButton>button:hover{
background:#1D4ED8;
color:white;
}

textarea{
border-radius:12px !important;
}

.stDownloadButton>button{
background:#16A34A;
color:white;
border-radius:12px;
font-weight:bold;
width:100%;
}

</style>
""", unsafe_allow_html=True)

# =========================
# PDF Generator
# =========================

def create_pdf(text):

    temp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")

    pdf = canvas.Canvas(temp.name)

    y = 800

    for line in text.split("\n"):

        pdf.drawString(40, y, line[:110])

        y -= 20

        if y < 50:
            pdf.showPage()
            y = 800

    pdf.save()

    return temp.name

# =========================
# Sidebar
# =========================

st.sidebar.title("🎓 Student Mentor AI")

feature = st.sidebar.selectbox(
    "Select Feature",
    [
        "AI Tutor",
        "Lecture Notes Summarizer",
        "Quiz Generator",
        "Flashcard Generator",
        "Exam Preparation Sheet"
    ]
)

language = st.sidebar.selectbox(
    "Select Language",
    [
        "English",
        "Roman Urdu",
        "Roman English"
    ]
)

st.sidebar.markdown("---")
st.sidebar.success("Powered by Groq AI 🚀")

# =========================
# Heading
# =========================

st.title("🎓 Student Mentor AI")

st.markdown(
"<h4 style='text-align:center;color:gray;'>Your Intelligent Academic Assistant</h4>",
unsafe_allow_html=True
)

st.write("")

user_input = st.text_area(
    "Enter your Question or Lecture Notes",
    height=220
)

# =========================
# File Upload
# =========================

uploaded_file = st.file_uploader(
    "📄 Upload Lecture Notes",
    type=["txt", "pdf"]
)

if uploaded_file is not None:

    if uploaded_file.type == "text/plain":
        user_input = uploaded_file.read().decode("utf-8")

    elif uploaded_file.type == "application/pdf":
        import PyPDF2

        pdf_reader = PyPDF2.PdfReader(uploaded_file)

        text = ""

        for page in pdf_reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"

        user_input = text


# =========================
# Language Prompt
# =========================

if language == "English":
    lang_prompt = "Reply only in simple English."

elif language == "Roman Urdu":
    lang_prompt = "Reply only in Roman Urdu. Never use Urdu script."

else:
    lang_prompt = "Reply in Roman English using easy English words."

# =========================
# Generate Button
# =========================

if st.button("🚀 Generate"):

    if user_input.strip() == "":
        st.warning("Please enter some text.")
        st.stop()

    if feature == "AI Tutor":

        prompt = f"""
{lang_prompt}

You are an AI Tutor.

Explain the following topic in very simple language.

Use headings and bullet points if needed.

Topic:
{user_input}
"""

    elif feature == "Lecture Notes Summarizer":

        prompt = f"""
{lang_prompt}

Summarize these lecture notes.

Make short exam notes.

Use headings.

Use bullet points.

Lecture Notes:

{user_input}
"""

    elif feature == "Quiz Generator":

        prompt = f"""
{lang_prompt}

Generate 10 Multiple Choice Questions.

After each MCQ write the correct answer.

Topic:

{user_input}
"""

    elif feature == "Flashcard Generator":

        prompt = f"""
{lang_prompt}

Create flashcards.

Format:

Question:
Answer:

Topic:

{user_input}
"""

    else:

        prompt = f"""
{lang_prompt}

Prepare an Exam Preparation Sheet.

Include:

1. Important Points

2. Definitions

3. Short Questions

4. Long Questions

5. MCQs with Answers

6. Tips for Exam

Topic:

{user_input}
"""

    with st.spinner("Generating Response..."):

        response = client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role": "system",
                    "content": "You are a friendly Student Mentor AI."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.5,
            max_tokens=1500

        )

        result = response.choices[0].message.content

    st.success("Response Generated Successfully ✅")

    st.subheader("📖 Result")

    st.write(result)

    pdf_file = create_pdf(result)

    with open(pdf_file, "rb") as file:

        st.download_button(

            label="📄 Download PDF",

            data=file,

            file_name="Student_Mentor_AI_Notes.pdf",

            mime="application/pdf"
        )
