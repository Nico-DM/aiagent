import os
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a specified Python file with optional arguments, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="A list of arguments to pass to the Python file.",
                items=types.Schema(type=types.Type.STRING),
            ),
        },
    ),
)

def run_python_file(working_directory, file_path="", args=[]):
    try:
        if not file_path:
            return 'Error: file_path is required'
        absolute_working_directory = os.path.abspath(working_directory)
        absolute_path = os.path.abspath(os.path.join(absolute_working_directory, file_path))
        if os.path.commonpath([absolute_path, absolute_working_directory]) != absolute_working_directory:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(absolute_path):
            return f'Error: File "{file_path}" not found.'
        if not absolute_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'
        try:
            completed_process = subprocess.run(["python3", absolute_path] + args, timeout=30, capture_output=True, cwd=absolute_working_directory)
        except Exception as e:
            return f"Error: executing Python file: {e}"

        if not completed_process.stdout:
            return "No output produced."
        output = "STDOUT: " + completed_process.stdout.decode() + "\nSTDERR: " + completed_process.stderr.decode()
        if completed_process.returncode != 0:
            output += f"\nProcess exited with code {completed_process.returncode}."
        return output

    except Exception as e:
        return f'Error: {str(e)}'