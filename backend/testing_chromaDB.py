import os
from dotenv import load_dotenv
import chromadb

# This finds the directory where THIS script is saved
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))
import google.generativeai as genai
from chromadb.utils.embedding_functions import GoogleGenerativeAiEmbeddingFunction

# 1. Setup
api_key = os.environ.get("GEMINI_API_KEY")
client = chromadb.PersistentClient(path="/home/sruthi_korlakunta/my-website/backend/ChromaDB_Blogs") # Points to where your files are
embedding_fn = GoogleGenerativeAiEmbeddingFunction(api_key=api_key)

# 2. Connect to the collection you created
collection = client.get_collection(name="blogs", embedding_function=embedding_fn)

# 3. Ask a test question
query_text = "What does Sruthi say about having hate in her system?"
results = collection.query(
    query_texts=[query_text],
    n_results=1 # Give me the top 1 match
)

# 4. Print the result
print("\n--- Match Found ---")
print(f"Title: {results['metadatas'][0][0]['title']}")
print(f"Excerpt: {results['documents'][0][0][:200]}...")