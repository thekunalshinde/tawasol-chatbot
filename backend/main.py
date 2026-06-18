import os
from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
from rag import search_knowledge

load_dotenv()

app = FastAPI()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class ChatRequest(BaseModel):
    question: str

@app.get("/")
def root():
    return {"status": "Tawasol Amal Chatbot API is running"}

@app.post("/chat")
def chat(request: ChatRequest):
    context = search_knowledge(request.question)
    
    prompt = f"""You are a helpful assistant for Tawasol Amal CRM — the STC internal CRM used by sales agents and testers.

Use ONLY the following knowledge to answer the question. If the answer is not in the knowledge, say "I don't have information about that yet. Please ask your senior or add it to the knowledge base."

KNOWLEDGE:
{context}

QUESTION: {request.question}

Give a clear, step-by-step answer. Be specific to Tawasol Amal."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=1024
    )
    
    answer = response.choices[0].message.content
    return {"answer": answer}