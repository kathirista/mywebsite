import os
from dotenv import load_dotenv

# This finds the directory where THIS script is saved
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))
import chromadb
from google import genai
from chromadb.api.types import Documents, Embeddings, EmbeddingFunction

# 1. API Configuration
API_KEY = os.environ.get("GEMINI_API_KEY")

if not API_KEY:
    print("❌ ERROR: API Key not found! Check your .env file.")
else:
    print(f"✅ API Key loaded: {API_KEY[:5]}...") # Prints only the first 5 characters for safety

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "ChromaDB_Blogs")

# 2. Embedding Function (Must match the one used during indexing)
class NewGoogleEmbeddingFunction(EmbeddingFunction):
    def __init__(self, api_key, model_name="models/gemini-embedding-001"):
        self.client = genai.Client(api_key=api_key)
        self.model_name = model_name

    def __call__(self, input: Documents) -> Embeddings:
        response = self.client.models.embed_content(
            model=self.model_name,
            contents=input
        )
        return [e.values for e in response.embeddings]

# 3. Initialize Clients
embedding_fn = NewGoogleEmbeddingFunction(api_key=API_KEY)
ABS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "ChromaDB_Blogs"))
chroma_client = chromadb.PersistentClient(path=ABS_PATH)
collection = chroma_client.get_collection(name="blogs", embedding_function=embedding_fn)


genai_client = genai.Client(api_key=API_KEY)

def what_would_sruthi_say(user_query):
    # Retrieve top 3 matching blogs
    results = collection.query(query_texts=[user_query], n_results=3)
    context_text = "\n\n".join(results['documents'][0])
    
    # Simple prompt structure to avoid Pydantic errors
    full_prompt = f"""
    You are Sruthi Korlakunta's AI twin. You are funny, optimistic, and realistic. 
    1. Use the "Blog Context" below to answer the user.
    2. If the context doesn't have the specific answer, use your general knowledge but 
       mention: "I haven't blogged about this specific detail yet, but as your AI twin, here's my take..."
    3. Keep it under 6 sentences. Mention Hyderabad or Germany if it fits!
    "
    
    Context from Sruthi's Blogs:
    {context_text}
    
    User Question: {user_query}
    """
    
    response = genai_client.models.generate_content(
        model="gemini-2.5-flash",
        contents=full_prompt
    )
    return response.text

if __name__ == "__main__":
    print("Sruthi AI is ready. Type 'exit' to quit.")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ['exit', 'quit']:
            break
        try:
            answer = what_would_sruthi_say(user_input)
            print(f"\nSruthi AI: {answer}")
        except Exception as e:
            print(f"\nError: {e}")