import os
import json

class FileReadError(Exception):
    pass

class FileWriteError(Exception):
    pass

def read_json_file(filepath):
    if not os.path.exists(filepath):
        raise FileReadError(f"File not found: {filepath}")
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
        return data
    except json.JSONDecodeError as e:
        raise FileReadError(f"Error decoding JSON from {filepath}: {e}")
    except Exception as e:
        raise FileReadError(f"Unexpected error reading {filepath}: {e}")


def write_json_file(filepath, data):
    try:
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        raise FileWriteError(f"Error writing to file {filepath}: {e}")
    except Exception as e:
        raise FileWriteError(f"Unexpected error writing to {filepath}: {e}")


def safe_execute(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        print(f"Error executing function {func.__name__}: {e}")
        return None