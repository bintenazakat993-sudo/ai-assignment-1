AI Assignment 1 – Machine Learning Model & AI Agent

Submitted By

Name: Aneesa Nazakat
Course: Artificial Intelligence
Semester: 5th Semester BSCS
Instructor: Touqeer Abbas

---

Project Overview

This repository contains the complete implementation of Assignment #1 for the Artificial Intelligence course. The assignment consists of two major tasks:

1. Task 1 – Machine Learning Model Training & Improvement
2. Task 2 – AI Agent Web Application using Gemini API

The project demonstrates practical implementation of Machine Learning concepts and AI-powered chatbot development using Python and Streamlit.

---

Repository Structure

ai-assignment-1/
│
├── README.md
│
├── task1-ml-model/
│   ├── model_training.ipynb
│   ├── dataset.csv
│   ├── report.pdf
│
├── task2-ai-agent/
│   ├── app.py
│   ├── requirements.txt
│   ├── .env.example
│   ├── screenshots/
│

---

Task 1 – Machine Learning Model

Objective

The objective of this task is to train, evaluate, and improve a Machine Learning model using a real-world dataset.

The selected dataset analyzes the impact of AI usage on student academic performance and burnout risk.

---

Dataset Information

Dataset Name

AI Student Impact Dataset

Dataset Features

- Student_ID
- Major_Category
- Year_of_Study
- Pre_Semester_GPA
- Weekly_GenAI_Hours
- Primary_Use_Case
- Prompt_Engineering_Skill
- Tool_Diversity
- Paid_Subscription
- Traditional_Study_Hours
- Perceived_AI_Dependency
- Institutional_Policy
- Anxiety_Level_During_Exams
- Post_Semester_GPA
- Skill_Retention_Score
- Burnout_Risk_Level

---

Machine Learning Workflow

The following Machine Learning steps were implemented:

1. Data Loading & Exploration

- Loaded dataset using Pandas
- Displayed:
  - ".head()"
  - ".shape"
  - ".info()"
  - ".describe()"
- Checked:
  - Missing values
  - Duplicate values

---

2. Data Preprocessing

Performed preprocessing steps including:

- Label Encoding
- Handling categorical variables
- Train-Test Splitting
- Feature selection

---

3. Model Training

Baseline Model

- Random Forest Classifier

Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

---

4. Model Improvement

The following improvement techniques were applied:

- Hyperparameter tuning
- Cross-validation

Accuracy Comparison

Model| Accuracy
Baseline Random Forest| 51.43%
Improved Random Forest| 53%

---

Task 2 – AI Agent Web Application

Objective

The objective of this task is to build an AI-powered chatbot using a free Large Language Model API and deploy it as a web application.

---

AI Agent Description

Project Name

AI Study Assistant

The chatbot helps students by answering educational and programming-related questions in simple language.

---
Features

- AI-powered chatbot
- Beginner-friendly responses
- Educational assistance
- Real-time Gemini API integration
- Simple and responsive web interface

---

Technologies Used

Programming Language

- Python

Framework

- Streamlit

API

- Google Gemini API

Python Libraries

- streamlit
- google-generativeai
- python-dotenv

---

Installation Guide

Step 1 – Clone Repository

git clone https://github.com/your-username/ai-assignment-1.git

---

Step 2 – Navigate to Project Folder

cd ai-assignment-1/task2-ai-agent

---

Step 3 – Install Dependencies

pip install -r requirements.txt

---

Step 4 – Create Environment File

Create a ".env" file and add your Gemini API key:

GEMINI_API_KEY=your_api_key_here

---

Step 5 – Run the Application

streamlit run app.py

---

Screenshots

Add screenshots of:

- Working chatbot interface
- ML model outputs
- Confusion matrix
- Accuracy graphs

inside the "screenshots/" folder.

---

Deployment

The chatbot can be deployed using:

- Streamlit Cloud
- GitHub
- Render
- Hugging Face Spaces

---

Sample Questions for AI Agent

Users can ask questions such as:

- What is Artificial Intelligence?
- Explain Machine Learning.
- What is Python?
- Explain loops in Python.
- Difference between AI and ML.

---

Learning Outcomes

Through this assignment, the following concepts were learned:

- Machine Learning workflow
- Data preprocessing
- Model evaluation
- Hyperparameter tuning
- AI chatbot development
- API integration
- Streamlit deployment
- GitHub project management

---

References

- Python Documentation
- Scikit-learn Documentation
- Pandas Documentation
- Streamlit Documentation
- Google Gemini API Documentation

---

Conclusion

This project successfully demonstrates the implementation of both Machine Learning and AI Agent development concepts.

The Machine Learning model predicts student burnout risk using educational and AI-usage related features, while the AI Study Assistant provides intelligent educational support using the Gemini API.

The assignment helped develop practical skills in:

- Machine Learning
- Data analysis
- API integration
- Web application development
- AI deployment

---
