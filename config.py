import json
import os

class ConfigError(Exception):
    pass

class Config:
    def __init__(self, config_file):
        self.config_file = config_file
        self.settings = self.load_config()

    def load_config(self):
        if not os.path.exists(self.config_file):
            raise ConfigError(f'Configuration file {self.config_file} does not exist.')
        try:
            with open(self.config_file, 'r') as file:
                settings = json.load(file)
        except json.JSONDecodeError:
            raise ConfigError(f'Error parsing JSON from {self.config_file}.')
        if not isinstance(settings, dict):
            raise ConfigError(f'Configuration file {self.config_file} must contain a JSON object.')
        return settings

    def get_setting(self, key, default=None):
        if key not in self.settings:
            if default is not None:
                return default
            raise ConfigError(f'Setting {key} not found in the configuration.')
        return self.settings[key]

# Example of using the Config class
if __name__ == '__main__':
    try:
        config = Config('config.json')
        print(config.get_setting('click_interval', 0.1))
    except ConfigError as e:
        print(f'Configuration Error: {e}')