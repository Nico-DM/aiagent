import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from functions.call_function import call_function
from functions.get_file_content import schema_get_file_content
from functions.get_files_info import schema_get_files_info
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file,
    ]
)

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.

Do not ask the user for more information. Instead, use the available functions to gather any necessary details.
"""

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
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt
        )
    )
    
    if "--verbose" in sys.argv:
        print("User prompt:", prompt)
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    if response.function_calls and len(response.function_calls) > 0:
        for function_call in response.function_calls:
            function_call_result = call_function(function_call, verbose="--verbose" in sys.argv)
            if not function_call_result.parts[0].function_response.response:
                raise Exception
            if "--verbose" in sys.argv:
                print(f"-> {function_call_result.parts[0].function_response.response}")
    else:
        print(response.text)


if __name__ == "__main__":
    main()
