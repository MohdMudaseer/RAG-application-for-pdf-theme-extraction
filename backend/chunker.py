from langchain.text_splitter import CharacterTextSplitter

def chunk_text(text, doc_id):
    splitter = CharacterTextSplitter(chunk_size=800, chunk_overlap=150)
    chunks = splitter.split_text(text)
    return [{"content": chunk, "metadata": {"doc_id": doc_id}} for chunk in chunks]
