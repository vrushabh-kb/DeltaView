import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
print("API KEY FOUND:", bool(api_key))

if not api_key:
    print("❌ API key not found")
    exit()

try:
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2 .5-flash",
        contents="Say hello in one sentence."
    )

    print("\n✅ API WORKING")
    print("Response:", response.text)

except Exception as e:
    print("\n❌ ERROR OCCURRED:")
    print(e)