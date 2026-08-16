import json

class AutoClickerConfig:
    def __init__(self, config_file):
        self.config_file = config_file
        self.settings = self.load_config()

    def load_config(self):
        try:
            with open(self.config_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return self.default_config()
        except json.JSONDecodeError:
            raise ValueError('Invalid JSON format in configuration file.')

    def default_config(self):
        return {
            'click_interval': 0.1,
            'clicks_per_second': 10,
            'active': True
        }

    def save_config(self):
        with open(self.config_file, 'w') as file:
            json.dump(self.settings, file, indent=4)

    def update_setting(self, key, value):
        if key in self.settings:
            self.settings[key] = value
            self.save_config()
        else:
            raise KeyError(f"'{key}' not found in settings.")

# Usage Example
# config = AutoClickerConfig('config.json')
# config.update_setting('click_interval', 0.05)