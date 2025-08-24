import os
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

def get_files_info(working_directory, directory="."):
    try:
        absolute_working_directory = os.path.abspath(working_directory)
        absolute_path = os.path.abspath(os.path.join(absolute_working_directory, directory))
        if os.path.commonpath([absolute_path, absolute_working_directory]) != absolute_working_directory:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(absolute_path):
            return f'Error: "{directory}" is not a directory'

        dir_contents = os.listdir(absolute_path)
        output = []
        for name in dir_contents:
            path = os.path.join(absolute_path, name)
            file_size = os.path.getsize(path)
            is_dir = os.path.isdir(path)
            output.append(f"- {name}: file_size={file_size} bytes, is_dir={is_dir}")
        return "\n".join(output) if output else f'Error: No files found in the directory "{directory}".'
    except Exception as e:
        return f'Error: {str(e)}'