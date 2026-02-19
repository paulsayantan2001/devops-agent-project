import streamlit as st
from chroma_db import add_data
from summarize import summarize

st.set_page_config(page_title="DevOps Incident Agent", layout="wide")

st.title("DevOps Incident Agent (Gemini + ChromaDB)")

tab1, tab2 = st.tabs(["Ingest Data", "Ask Question"])

with tab1:
    text = st.text_area("Paste Incident Data", height=200)

    if st.button("Store Data"):
        if text.strip():
            add_data(text)
            st.success("Stored successfully!")
        else:
            st.warning("Please enter some text.")

with tab2:
    query = st.text_input("Ask Incident Question")

    if st.button("Analyze Incident"):
        if query.strip():
            answer = summarize(query)
            st.write(answer)
        else:
            st.warning("Please enter a question.")
