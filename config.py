import json
import os

def load_config(file_path='config.json'):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Config file not found: {file_path}")
    with open(file_path, 'r') as file:
        return json.load(file)


def save_config(data, file_path='config.json'):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def get_default_config():
    return {
        'setting1': 'value1',
        'setting2': 'value2',
        'setting3': 'value3'
    }


def validate_config(data):
    required_keys = ['setting1', 'setting2', 'setting3']
    for key in required_keys:
        if key not in data:
            raise ValueError(f'Missing required config key: {key}')