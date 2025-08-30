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

Do not respond directly to the user. Instead, use function calls to gather information or perform actions. Only respond to the user when you have completed their request.
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

    try:
        for i in range(20):
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

            for candidate in response.candidates:
                messages.append(candidate.content)
                for part in candidate.content.parts:
                    if part.function_call:
                        function_call = part.function_call
                        function_call_result = call_function(function_call, verbose="--verbose" in sys.argv)
                        if not function_call_result.parts[0].function_response.response:
                            raise Exception
                        messages.append(types.Content(role="user", parts=function_call_result.parts))
                        if "--verbose" in sys.argv:
                            print(f"-> {function_call_result.parts[0].function_response.response}")

            if response.text:
                print(response.text)
                break

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
