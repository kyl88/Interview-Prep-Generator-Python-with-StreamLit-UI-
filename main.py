import langchain as lch
import streamlit as st

st.title("PREP INTERVIEW  GENERATOR")

interview_question = st.sidebar.selectbox(
    "Enter your interview question here", ("Tell me more about yourself?"
                                          ,"What are your strengths"))

if interview_question == "Tell me more about yourself?":
    st.sidebar.text_area(label ="Enter a valid response",max_chars=300)