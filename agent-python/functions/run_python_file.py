import os
import subprocess

def run_python_file(working_directory, file_path, args=None):

    abs_working_dir = os.path.abspath(working_directory)
    full_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))

    try:
        if os.path.commonpath([abs_working_dir, full_file_path]) != abs_working_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory.'

        if not os.path.isfile(full_file_path):
            return f'Error: "{file_path}" does not exist'

        if full_file_path.endswith('.py'):
            command = ['python', full_file_path]
            if args:
                command.extend(args)
            result = subprocess.run(command, capture_output=True, text=True, timeout=30)

            err_code = "" if result.returncode == 0 else f'Error: Process exited with code {result.returncode}'
            std_str = f"STDOUT: {result.stdout}\nSTDERR: {result.stderr}" 

            return err_code + "\n" + std_str
        else:
            return f'Error: "{file_path}" is not a Python file'


    except Exception as e:
        return f'Error: executing Python file: {e}'

