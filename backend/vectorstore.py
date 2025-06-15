from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from sentence_transformers import SentenceTransformer
import torch

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

def store_documents(doc_chunks, persist_dir="chroma_db"):
    texts = [chunk["text"] for chunk in doc_chunks]
    metadatas = [{"source": chunk["doc_id"]} for chunk in doc_chunks]

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    vectordb = Chroma.from_texts(
        texts=texts,
        embedding=embeddings,
        metadatas=metadatas,
        persist_directory=persist_dir
    )
    vectordb.persist()
    return vectordb

