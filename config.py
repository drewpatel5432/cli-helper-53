import json
import os

def load_config(file_path='config.json', defaults=None):
    if defaults is None:
        defaults = {}
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            config = json.load(f)
            return {**defaults, **config}
    return defaults

def save_config(file_path='config.json', config=None):
    if config is None:
        config = {}
    with open(file_path, 'w') as f:
        json.dump(config, f, indent=4)

# Usage example
if __name__ == '__main__':
    defaults = {'click_rate': 10, 'duration': 60}
    config = load_config(defaults=defaults)
    print(config)