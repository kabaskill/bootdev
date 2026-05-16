import os

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    full_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))

    try:
        if os.path.commonpath([abs_working_dir, full_file_path]) != abs_working_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(full_file_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        parent_dir = os.path.dirname(full_file_path)
        os.makedirs(parent_dir, exist_ok=True)

        with open(full_file_path, "w") as f:
            f.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f'Error: Validating file path "{file_path}": {e}'
