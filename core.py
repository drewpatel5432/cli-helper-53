import json
import os

class DataProcessor:
    def __init__(self, data_file):
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        if not os.path.exists(self.data_file):
            raise FileNotFoundError(f"{self.data_file} does not exist")
        with open(self.data_file, 'r') as file:
            return json.load(file)

    def process_data(self):
        # Example transformation: convert values to uppercase
        return {key: value.upper() for key, value in self.data.items()}

    def save_data(self, output_file):
        with open(output_file, 'w') as file:
            json.dump(self.process_data(), file, indent=2)

if __name__ == '__main__':
    processor = DataProcessor('input.json')
    processor.save_data('output.json')
