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
 from transformers import pipeline

# Load once when the module is imported
qa_pipeline = pipeline("question-answering", model="deepset/tinyroberta-squad2")

def answer_with_llm(user_question, context):
    result = qa_pipeline(question=user_question, context=context)
    return result['answer']

def build_context_from_csv(df):
    context = "\n".join(df.apply(lambda x: f"Q: {x['Question']} A: {x['Answer']}", axis=1))
    return context       
