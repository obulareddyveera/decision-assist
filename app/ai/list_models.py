import os
from google import genai
from dotenv import load_dotenv
load_dotenv()  # <-- REQUIRED for standalone scripts


api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise RuntimeError("GOOGLE_API_KEY not found in environment")

client = genai.Client(api_key=api_key)

print("Available Gemini models:\n")

for model in client.models.list():
    print(model.name)
