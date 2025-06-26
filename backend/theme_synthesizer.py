from langchain_groq import ChatGroq

def identify_themes_across_docs(text_blocks):
    prompt = f"""
You are an AI document analyst. You will be given multiple documents (text extracted from various sources such as reports, memos, emails, articles, contracts, etc.).

Your job is to analyze and extract insights in the following format:

---

**PART 1: Individual Document Responses**

For each document, extract the most relevant statement, insight, or finding along with its source citation (such as "Page X, Paragraph Y" or any positional marker available).

Present the output in a table format like this:

Document ID | Extracted Answer | Citation  
----------- | ---------------- | --------  
DOC001 | The report concludes that sales dropped due to product delivery issues. | Page 3, Para 2  
DOC002 | The memo emphasizes the need for employee upskilling to meet Q3 goals. | Page 1, Para 4  

---

**PART 2: Final Synthesized Response (Themes)**

Identify common themes across the documents based on their extracted answers.

For each theme:
- Give it a short title
- Write a concise summary (1–2 lines)
- List the relevant Document IDs

Present in this format:

**Theme 1 – Operational Challenges:**  
Documents (DOC001, DOC003) discuss issues related to delivery delays and team capacity.

**Theme 2 – Strategic Recommendations:**  
DOC002 outlines upskilling initiatives to improve quarterly performance.

---

Now analyze the following documents and return the results in the specified format:
{text_blocks}
"""
    llm = ChatGroq(model_name="llama3-8b-8192")
    return llm.predict(prompt)
