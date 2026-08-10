import json
import os

DEFAULT_CONFIG = {
    'host': 'localhost',
    'port': 8080,
    'debug': False,
    'log_level': 'WARNING'
}

class ConfigLoader:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                config_data = json.load(f)
            return {**DEFAULT_CONFIG, **config_data}
        return DEFAULT_CONFIG

    def get(self, key, default=None):
        return self.config.get(key, default)

    def __getitem__(self, key):
        return self.config[key]

    def __repr__(self):
        return f'<ConfigLoader {self.config}>'
