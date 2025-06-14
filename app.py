import streamlit as st
import pandas as pd
import os
from backend.extractor import extract_text_from_pdf
from backend.chunker import chunk_text
from backend.vectorstore import store_documents
from backend.qa_engine import create_chat_chain
from backend.theme_synthesizer import identify_themes_across_docs

st.set_page_config(page_title="📚 Multi-Doc Research Chatbot", layout="wide")
st.title("📄 Document Research & Theme Identification Chatbot")
st.markdown("Upload multiple **PDFs or scanned images**. Get citation-backed answers and synthesized themes across documents.")

if "chatbot" not in st.session_state:
    st.session_state.chatbot = None
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None
if "all_chunks" not in st.session_state:
    st.session_state.all_chunks = []
if "doc_texts" not in st.session_state:
    st.session_state.doc_texts = {}

with st.sidebar:
    st.header("📂 Upload Documents")
    uploaded_files = st.file_uploader("Upload PDFs", type=["pdf"], accept_multiple_files=True)
    if uploaded_files and st.button("📌 Process Documents"):
        all_chunks = []
        all_text_blocks = []

        for idx, file in enumerate(uploaded_files):
            doc_id = f"DOC{idx+1:03}"
            st.info(f"Processing {doc_id}: {file.name}")
            text = extract_text_from_pdf(file)
            st.session_state.doc_texts[doc_id] = text
            chunks = chunk_text(text, doc_id)
            all_chunks.extend(chunks)
            all_text_blocks.append(f"{doc_id}: {text}")

        st.session_state.vectorstore = store_documents(all_chunks)
        st.session_state.chatbot = create_chat_chain(st.session_state.vectorstore)
        st.session_state.all_chunks = all_chunks
        st.success("✅ All documents processed!")

if st.session_state.chatbot:
    query = st.text_input("💬 Ask a question across documents")
    if query:
        with st.spinner("Thinking..."):
            from backend.qa_engine import get_cited_response
            cited_answers = get_cited_response(st.session_state.chatbot, query)
            st.subheader("📑 Cited Responses")
            df = pd.DataFrame(cited_answers, columns=["Document ID", "Extracted Answer", "Citation"])
            st.dataframe(df)

    if st.button("🔍 Identify Themes Across Documents"):
        with st.spinner("Analyzing themes..."):
            combined_text = "\n".join(st.session_state.doc_texts.values())
            theme_result = identify_themes_across_docs(combined_text)
            st.subheader("🧠 Identified Themes")
            st.markdown(theme_result)
