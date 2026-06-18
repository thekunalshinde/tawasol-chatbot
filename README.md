# Tawasol Amal AI Chatbot

An AI-powered RAG chatbot for Tawasol Amal CRM — STC internal testing assistant.

## Tech Stack
- **LLM:** Groq API (Llama 3.3)
- **RAG:** ChromaDB
- **Backend:** FastAPI (Python)
- **Frontend:** Streamlit

## How to Run

### Backend
```bash
cd backend
venv\Scripts\activate
uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
streamlit run app.py
```

## Project Structure
```
tawasol-chatbot/
├── backend/
│   ├── knowledge/workflows.txt
│   ├── main.py
│   ├── rag.py
│   └── requirements.txt
└── frontend/
    └── app.py
```