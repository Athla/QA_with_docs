import streamlit as st
from model_processing import retrieve_and_answer as QA
from model_processing import load_split_docs, create_vectorstore

st.title("**Welcome to the **:red[World Library]**, how can I assist you?**")
st.markdown("***")
st.header("The **:red[World Library]** will assist you with questions related to the details of the World of :blue[Pathfinder].")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    st.markdown(message["content"])

with st.spinner("Loading the contents of the **:red[World Library]**"):
    splits = load_split_docs("src")
    store = create_vectorstore(splits)

if prompt := st.chat_input("What is your question, wanderer of the World Library?"):
    st.session_state.messages.append({"role":"user", "content":prompt})

    with st.spinner("Wait! We're looking through the World Library"):
        message_placeholder = st.empty()
        response = QA(prompt)
        message_placeholder.markdown(response)
        st.session_state.messages.append({"role":"assistant", "content":response},)