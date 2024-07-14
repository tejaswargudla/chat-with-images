from langchain_community.vectorstores import FAISS
import streamlit as st
import langfuse
import os
from dotenv import dotenv_values
from src.utils.access import is_exists
from src.utils.embeddings import get_embeddings

embedding_model = get_embeddings()
cfg = dotenv_values(".env")

faiss = FAISS.load_local("faiss_data",
                         embeddings= embedding_model,
                         normalize_L2 = True,
                         allow_dangerous_deserialization=True)
st.title("Chat With your Images")
prompt = "Hello"
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    faiss_op = faiss.similarity_search_with_relevance_scores(prompt)
    
    images = [doc.metadata.get("imagepath") for doc, score in faiss_op if score > float(cfg.get("min_score_threshold"))]
    if images:
        response = f"Echo: {st.image(images, width=300)}"
    else:
        response = "Echo: Didnt find any pics in the repository."
    
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    