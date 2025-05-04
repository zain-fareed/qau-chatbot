import streamlit as st
import pandas as pd
from difflib import get_close_matches

# Load CSV file
@st.cache_data
def load_data():
    return pd.read_csv(r"C:\Users\COMPUTER WORLD\OneDrive\Desktop\qau_programs_all.csv.txt.csv")

qa_data = load_data()

# Chatbot logic
def smart_chatbot(user_question, qa_data):
    questions = qa_data['Question'].tolist()
    match = get_close_matches(user_question, questions, n=1, cutoff=0.5)

    if match:
        answer = qa_data[qa_data['Question'] == match[0]]['Answer'].values[0]
        return f"*Q:* {match[0]}\n\n*A:* {answer}"
    else:
        return "Sorry, I couldn't find a relevant answer."

# Streamlit UI
st.title("QAU Chatbot - Ask About Quaid-e-Azam University")
st.markdown("Ask about programs, fees, eligibility, etc.")

# Example buttons
st.subheader("Example Questions:")
col1, col2 = st.columns(2)

with col1:
    if st.button("What BS programs are offered?"):
        st.session_state['example'] = "What undergraduate programs does QAU offer in Natural Sciences?"
    if st.button("Does QAU offer CS?"):
        st.session_state['example'] = "Does QAU offer BS in Computer Science?"

with col2:
    if st.button("What is the BS fee?"):
        st.session_state['example'] = "What is the fee structure for BS programs at QAU?"
    if st.button("Eligibility for BS?"):
        st.session_state['example'] = "What is the eligibility criterion for admission to BS programs at QAU?"

# Display selected question
user_input = st.text_input("Your question:", value=st.session_state.get('example', ''))

if user_input:
    result = smart_chatbot(user_input, qa_data)
    st.markdown(result)
