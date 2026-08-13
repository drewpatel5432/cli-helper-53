import json

class ClickDataValidator:
    def __init__(self, data):
        self.data = data

    def is_valid_click_data(self):
        return all([self._is_valid_coordinate(click) for click in self.data.get('clicks', [])])

    def _is_valid_coordinate(self, click):
        return isinstance(click, dict) and 'x' in click and 'y' in click and self._is_within_bounds(click['x'], click['y'])

    def _is_within_bounds(self, x, y, min_bound=0, max_bound=1920):
        return min_bound <= x <= max_bound and min_bound <= y <= max_bound

def validate_click_data(json_str):
    try:
        data = json.loads(json_str)
        validator = ClickDataValidator(data)
        return validator.is_valid_click_data()
    except (json.JSONDecodeError, KeyError):
        return False

# Example of usage
if __name__ == '__main__':
    json_input = '{"clicks": [{"x": 100, "y": 200}, {"x": 300, "y": 400}]}'
    print(validate_click_data(json_input))  # Should return True
