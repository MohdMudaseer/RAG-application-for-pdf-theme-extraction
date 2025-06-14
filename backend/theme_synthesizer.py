from langchain_groq import ChatGroq

def identify_themes_across_docs(text_blocks):
    prompt = f"Analyze the following texts and identify key themes. Return themes with document references:\n{text_blocks}"
    llm = ChatGroq(model_name="llama3-8b-8192")
    return llm.predict(prompt)
