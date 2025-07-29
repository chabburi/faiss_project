

import streamlit as st
from pypdf import PdfReader 
from embedding import create_embeddings
from retrieveing import answering_user_question

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

if "placeholder" not in st.session_state:
    st.session_state.placeholder = "Enter query here"

st.title("Local RAG Chatbot")
st.markdown(
    '''
    Welcome to RAG Chatbot. 

    We Provide:
    1. Creating embeddings for the input file.
    2. Get status of your issue using user id.
    '''
)

genre = st.radio(
    "Please provide the Operation you want to perform",
    ["Embedding", "Retrieveing"],
    captions=[
        "Create embeddings for the given file",
        "Query the document",
    ],
)

# === Retrieveing Block ===
if genre == "Retrieveing":
    text_input = st.text_input(
        "Please enter your query below 👇",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder=st.session_state.placeholder,
    )
    if st.button("Submit"):
        if text_input.strip():
            response = answering_user_question(text_input)
            st.write(response)
        else:
            st.warning("Please provide input query.")

# === Embedding Block ===
if genre == "Embedding":
    uploaded_file = st.file_uploader("Please upload the document for creating embeddings.")
    if st.button("Submit"):
        if uploaded_file is not None:
            reader = PdfReader(uploaded_file)
            full_text = ''
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    full_text += text + '\n'
            response = create_embeddings(full_text)
            st.write(response)
        else:
            st.warning("Please upload a file.")