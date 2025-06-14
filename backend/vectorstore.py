from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

def store_documents(doc_chunks, persist_dir="chroma_db"):
    texts = [chunk["content"] for chunk in doc_chunks]
    metadatas = [chunk["metadata"] for chunk in doc_chunks]
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectordb = Chroma.from_texts(texts, embedding=embeddings, metadatas=metadatas, persist_directory=persist_dir)
    vectordb.persist()
    return vectordb
