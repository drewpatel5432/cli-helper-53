import json
import os

class Config:
    def __init__(self, filepath):
        self.filepath = filepath
        self.settings = self.load_config()

    def load_config(self):
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"Configuration file not found: {self.filepath}")
        try:
            with open(self.filepath, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            raise ValueError(f"Error decoding JSON from the configuration file: {self.filepath}")
        except Exception as e:
            raise RuntimeError(f"Unexpected error occurred while loading config: {e}")

    def get(self, key, default=None):
        if key not in self.settings:
            if default is None:
                raise KeyError(f"Key not found in config: {key}")
            return default
        return self.settings[key]

    def set(self, key, value):
        self.settings[key] = value
        self.save_config()

    def save_config(self):
        try:
            with open(self.filepath, 'w') as file:
                json.dump(self.settings, file, indent=4)
        except Exception as e:
            raise RuntimeError(f"Error saving config: {e}")

config = Config('config.json')