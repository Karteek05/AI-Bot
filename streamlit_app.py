import streamlit as st
from app import summarize_text

st.title("Tiny AI Summarizer")
article = st.text_area("Paste a news article or blog text:")
if st.button("Summarize"):
    if article:
        summary = summarize_text(article)
        st.subheader("Summary:")
        st.write(summary)
    else:
        st.warning("Please enter some text to summarize.")