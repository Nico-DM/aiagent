import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    if len(sys.argv) < 2:
        print("Error: missing prompt")
        sys.exit(1)
    prompt = sys.argv[1]
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages
    )
    print(response.text)
    print("Prompt tokens:", response.usage_metadata.prompt_token_count) # type: ignore
    print("Response tokens:", response.usage_metadata.candidates_token_count) # type: ignore


if __name__ == "__main__":
    main()
