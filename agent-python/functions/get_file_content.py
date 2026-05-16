import os

from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    full_file_path = os.path.join(abs_working_dir, file_path)

    try:
        if os.path.commonpath([abs_working_dir, full_file_path]) != abs_working_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory.'

        if not os.path.isfile(full_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(full_file_path, "r") as f:
            content = f.read(MAX_CHARS)

            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'


    except Exception as e:
        return f'Error: reading file "{file_path}": {e}'

    return content
 
