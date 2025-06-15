from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_groq import ChatGroq

def create_chat_chain(vectordb):
    llm = ChatGroq(model_name="llama3-8b-8192", temperature=0.2)
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    retriever = vectordb.as_retriever(search_kwargs={"k": 4})
    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        return_source_documents=True
    )

def get_cited_response(chain, query):
    result = chain.invoke({"question": query})
    sources = result.get("source_documents", [])
    answer = result.get("answer", "")
    citations = []
    for doc in sources:
        citations.append([
            doc.metadata.get("source", "Unknown"),
            doc.page_content.strip()[:200] + "...",
            doc.metadata.get("source", "Unknown")
        ])
    return citations
