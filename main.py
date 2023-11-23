import langchain as lch
import streamlit as st

st.title("PREP INTERVIEW  GENERATOR")

interview_question = st.sidebar.selectbox(
    "Enter your interview question here", ("Tell me more about yourself?"
                                        ,"What are your strengths and weaknesses?"
                                        ,"Why do you want to work here?"
                                        ,"Have you been in a difficult situation and how did you handle it?"
                                        ,"Discuss the possible long-term work objectives working as a data analyst?"
                                        ,"Discuss the possible skills needed to become a data analyst?"
                                        ,"List the different types of data?"
                                        ,"Describe the difference between supervised and unsupervised learning?"
                                        ,"Explain the difference between classification and regression algorithms"
                                        ,"What programming languages and libraries do you use for data analysts?"
                                        ,"How to handle missing or null values in a dataset?"
                                        ,"What is an Outlier Detection?"
                                        ,"How do you identify outliers in the dataset?"
                                        ,"Describe methods to deal with imbalanced datasets?"
                                        ,"Discuss any data visualization tools you worked with?"
                                        ,"Discuss a specific project where you analysed and cleaned a dataset to gain insights about the data?"))

if interview_question == "Tell me more about yourself?":
    st.sidebar.text_area(label ="Enter a valid response",max_chars=300)

if interview_question == "What are your strengths and weaknesses?":
   interview_question =  st.sidebar.text_area(label ="Enter a valid response",max_chars=300)

if interview_question == "Why do you want to work here?":
    st.sidebar.text_area(label ="Enter a valid response",max_chars=300)

if interview_question == "Have you been in a difficult situation and how did you handle it?":
    st.sidebar.text_area(label ="Enter a valid response",max_chars=300)

if interview_question == "Discuss the possible long-term work objectives working as a data analyst?":
    st.sidebar.text_area(label ="Enter a valid response",max_chars=300)

if interview_question == "What are your strengths and weaknesses?":
    st.sidebar.text_area(label ="Enter a valid response",max_chars=300)

if interview_question == "Discuss the possible skills needed to become a data analyst?":
    st.sidebar.text_area(label ="Enter a valid response",max_chars=300)

if interview_question == "List the different types of data?":
    st.sidebar.text_area(label ="Enter a valid response",max_chars=300)

if interview_question == "Describe the difference between supervised and unsupervised learning?":
    st.sidebar.text_area(label ="Enter a valid response",max_chars=300)

if interview_question == "Explain the difference between classification and regression algorithms?":
    st.sidebar.text_area(label ="Enter a valid response",max_chars=300)

if interview_question == "What programming languages and libraries do you use for data analysts?":
    st.sidebar.text_area(label ="Enter a valid response",max_chars=300)

if interview_question == "How to handle missing or null values in a dataset?":
    st.sidebar.text_area(label ="Enter a valid response",max_chars=300)

if interview_question == "What is an Outlier Detection?":
    st.sidebar.text_area(label ="Enter a valid response",max_chars=300)

if interview_question == "How do you identify outliers in the dataset?":
    st.sidebar.text_area(label ="Enter a valid response",max_chars=300)

if interview_question == "Describe methods to deal with imbalanced datasets?":
    st.sidebar.text_area(label ="Enter a valid response",max_chars=300)

if interview_question == "Discuss any data visualization tools you worked with?":
    st.sidebar.text_area(label ="Enter a valid response",max_chars=300)
    
if interview_question == "Discuss a specific project where you analysed and cleaned a dataset to gain insights about the data?":
    st.sidebar.text_area(label ="Enter a valid response",max_chars=300)