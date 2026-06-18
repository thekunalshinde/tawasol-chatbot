import os
import chromadb
from chromadb.utils import embedding_functions

KNOWLEDGE_DIR = os.path.join(os.path.dirname(__file__), "knowledge")
CHROMA_PATH = os.path.join(os.path.dirname(__file__), "chroma_db")

def load_knowledge():
    docs = []
    ids = []
    count = 0
    for filename in os.listdir(KNOWLEDGE_DIR):
        if filename.endswith(".txt"):
            filepath = os.path.join(KNOWLEDGE_DIR, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            chunks = [c.strip() for c in content.split("\n\n") if c.strip()]
            for chunk in chunks:
                docs.append(chunk)
                ids.append(f"doc_{count}")
                count += 1
    return docs, ids

def get_collection():
    client = chromadb.PersistentClient(path=CHROMA_PATH)
    ef = embedding_functions.DefaultEmbeddingFunction()
    collection = client.get_or_create_collection(
        name="tawasol_knowledge",
        embedding_function=ef
    )
    if collection.count() == 0:
        docs, ids = load_knowledge()
        collection.add(documents=docs, ids=ids)
        print(f"Loaded {len(docs)} knowledge chunks into ChromaDB")
    return collection

def search_knowledge(query: str, n_results: int = 3) -> str:
    collection = get_collection()
    results = collection.query(query_texts=[query], n_results=n_results)
    docs = results["documents"][0]
    return "\n\n---\n\n".join(docs)