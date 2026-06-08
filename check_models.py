import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
print(f"Using API Key: {api_key[:5]}...")

try:
    client = genai.Client(api_key=api_key)
    models = client.models.list()
    print("Available models:")
    count = 0
    for m in models:
        if 'gemini' in m.name.lower():
            print(f"- {m.name}")
            count += 1
            if count > 20: break
except Exception as e:
    print(f"Error: {e}")
