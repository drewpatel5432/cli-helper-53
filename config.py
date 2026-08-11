import json
import os

class ConfigLoader:
    def __init__(self, defaults=None):
        self.config = defaults or {}

    def load(self, filepath):
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                user_config = json.load(file)
                self.config.update(user_config)
        else:
            print(f'Configuration file {filepath} not found. Using defaults.\n')

    def get(self, key, default=None):
        return self.config.get(key, default)

    def __str__(self):
        return json.dumps(self.config, indent=2)

# Example Usage
if __name__ == '__main__':
    default_config = {
        'host': 'localhost',
        'port': 8080,
        'debug': False
    }
    config_loader = ConfigLoader(defaults=default_config)
    config_loader.load('config.json')
    print(config_loader)