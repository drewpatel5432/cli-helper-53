import json
import os

class ConfigLoader:
    def __init__(self, default_config_path='default_config.json'):
        self.default_config_path = default_config_path
        self.config = self.load_config()

    def load_config(self):
        config = self.load_default_config()
        env_config = self.load_env_config()
        config.update(env_config)
        return config

    def load_default_config(self):
        if os.path.exists(self.default_config_path):
            with open(self.default_config_path, 'r') as f:
                return json.load(f)
        return {}

    def load_env_config(self):
        env_config = {}
        for key, value in os.environ.items():
            if key.startswith('APP_'):
                env_config[key[4:].lower()] = value  # Remove APP_ prefix
        return env_config

# Example usage:
if __name__ == '__main__':
    config_loader = ConfigLoader()
    print(config_loader.config)