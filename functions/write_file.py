import os


def write_file(working_directory, file_path="", content=""):
    try:
        absolute_working_directory = os.path.abspath(working_directory)
        absolute_path = os.path.abspath(os.path.join(absolute_working_directory, file_path))
        # Verificación robusta usando os.path.commonpath
        if os.path.commonpath([absolute_path, absolute_working_directory]) != absolute_working_directory:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        with open(absolute_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f'Error: {str(e)}'