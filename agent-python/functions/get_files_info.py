import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_working_dir, directory))
        if os.path.commonpath([abs_working_dir, target_dir]) != abs_working_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        display_dir = directory if directory != "." else "current"

        files_info = []
        print(f"Result for '{display_dir}' directory:")
        for file in os.listdir(target_dir):
                full_path = os.path.join(target_dir, file)
                size = os.path.getsize(full_path)
                is_directory = os.path.isdir(full_path)
                files_info.append(f"- {file}: file_size={size}, is_dir={is_directory}")
        return "\n".join(files_info)

    except Exception as e:
        return f"Error listing files: {e}"

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)

