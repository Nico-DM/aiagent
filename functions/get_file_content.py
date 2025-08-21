import os
from config import MAX_CHARS


def get_file_content(working_directory, file_path=""):
    try:
        absolute_working_directory = os.path.abspath(working_directory)
        absolute_path = os.path.abspath(os.path.join(absolute_working_directory, file_path))
        # Verificación robusta usando os.path.commonpath
        if os.path.commonpath([absolute_path, absolute_working_directory]) != absolute_working_directory:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(absolute_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(absolute_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)

        if len(file_content_string) == MAX_CHARS:
            file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'

        return file_content_string
    except Exception as e:
        return f'Error: {str(e)}'