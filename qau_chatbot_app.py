import streamlit as st
import pandas as pd
from difflib import get_close_matches

# Load CSV directly from GitHub repo (no local path)
@st.cache_data
def load_data():
    return pd.read_csv("qau_programs_all.csv.csv")

qa_data = load_data()

# Simple chatbot logic
def smart_chatbot(user_input, qa_data):
    questions = qa_data['Question'].tolist()
    match = get_close_matches(user_input, questions, n=1, cutoff=0.6)
    if match:
        answer = qa_data.loc[qa_data['Question'] == match[0], 'Answer'].values[0]
        return f"Q: {match[0]}\n\nA: {answer}"
    else:
        return "Sorry, I couldn't find an answer to that."

# Streamlit UI
st.title("QAU Chatbot - Ask About Quaid-e-Azam University")
st.markdown("Ask about programs, fees, eligibility, etc.")

# Example questions
st.markdown("### Example Questions:")
cols = st.columns(2)
examples = [
    "What BS programs are offered?",
    "What is the BS fee?",
    "Does QAU offer BS in Computer Science?",
    "Eligibility for BS?"
]

for i, example in enumerate(examples):
    if cols[i % 2].button(example):
        st.session_state['example_question'] = example

# Input
user_input = st.text_input("Your question:", value=st.session_state.get('example_question', ''))
if user_input:
    result = smart_chatbot(user_input, qa_data)
    st.markdown(result)

