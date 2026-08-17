import os
import json

def load_config(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f'Config file not found: {file_path}')  
    
    try:
        with open(file_path, 'r') as config_file:
            config = json.load(config_file)
    except json.JSONDecodeError as e:
        raise ValueError(f'Error decoding JSON: {e}') from e
    
    required_keys = ['interval', 'clicks', 'duration']
    for key in required_keys:
        if key not in config:
            raise KeyError(f'Missing required config key: {key}')  
    
    return config

if __name__ == '__main__':
    config_file_path = 'config.json'
    try:
        config = load_config(config_file_path)
        print('Config loaded successfully:', config)
    except Exception as e:
        print(f'Failed to load config: {e}')