import os
from dotenv import load_dotenv
from google import genai

# This finds the directory where THIS script is saved
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

print("Available models for your key:")
for model in client.models.list():
    # We only care about models that support 'generateContent'
    if 'generateContent' in model.supported_actions:
        print(f" - {model.name}")