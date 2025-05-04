import pandas as pd
from difflib import get_close_matches

def load_data(filepath):
    return pd.read_csv(filepath)

def smart_chatbot(user_input, qa_data):
    questions = qa_data['Question'].tolist()
    matches = get_close_matches(user_input, questions, n=1, cutoff=0.6)
    if matches:
        answer = qa_data.loc[qa_data['Question'] == matches[0], 'Answer'].values[0]
        return f"Q: {matches[0]}\nA: {answer}"
    else:
        return "Sorry, I couldn't find an answer to that question."