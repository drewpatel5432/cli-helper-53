import time
import random

def validate_input(user_input):
    if not isinstance(user_input, dict):
        raise ValueError('Input must be a dictionary')
    if 'clicks' not in user_input or not isinstance(user_input['clicks'], int):
        raise ValueError('Missing or invalid number of clicks')
    if 'interval' not in user_input or not isinstance(user_input['interval'], (int, float)):
        raise ValueError('Missing or invalid interval')

class AutoClicker:
    def __init__(self, clicks, interval):
        self.clicks = clicks
        self.interval = interval

    def start(self):
        for _ in range(self.clicks):
            self.perform_click()
            time.sleep(self.interval)

    def perform_click(self):
        print('Click!')

if __name__ == '__main__':
    user_input = {'clicks': 5, 'interval': 1.0}
    try:
        validate_input(user_input)
        auto_clicker = AutoClicker(user_input['clicks'], user_input['interval'])
        auto_clicker.start()
    except ValueError as e:
        print(f'Input error: {e}')