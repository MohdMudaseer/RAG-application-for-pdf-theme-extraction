from langchain_groq import ChatGroq

def identify_themes_across_docs(text_blocks):
    prompt = f"""
You are an AI document analyst. Analyze the following texts and identify key themes.

Return each theme with:
- Theme Title
- A short summary
- A list of relevant Document IDs

Example format:
1. Theme Title
   - Summary: ...
   - Relevant Documents: DOC001, DOC002

Documents:
{text_blocks}
"""
    llm = ChatGroq(model_name="llama3-8b-8192")
    return llm.predict(prompt)
