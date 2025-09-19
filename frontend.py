

#Step1: Setup Upload PDF functionality
import streamlit as st

uploaded_file = st.file_uploader("Upload PDF",
                                 type="pdf",
                                 accept_multiple_files=True) # Allow multiple file uploads, if false, only single file upload

#Step2: Chatbot Skeleton (Question & Answer)
user_query = st.text_area("Enter the specification: ", height=150 , placeholder= "Ask for the Best Crop Recommendation") # Text area for user input

ask_question = st.button("Ask AI Bhagwan")

if ask_question:
    
    if uploaded_file:
        st.chat_message("user").write(user_query)

        #RAG Pipeline
        fixed_response = "This is a fixed response. Replace with RAG pipeline output."
        st.chat_message("AI Bhagwan").write(fixed_response)
    else:
        st.error("Please upload at least one PDF file to proceed.")
