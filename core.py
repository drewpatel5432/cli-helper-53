import time
import random
from validators import validate_input

class AutoClicker:
    def __init__(self, click_interval, total_clicks):
        self.click_interval = click_interval
        self.total_clicks = total_clicks

    def start_clicking(self):
        for i in range(self.total_clicks):
            if validate_input(self.click_interval):
                self.click()
            else:
                print('Invalid input. Skipping click.')
            time.sleep(self.click_interval)

    def click(self):
        print('Click!')  # Simulate a click

if __name__ == '__main__':
    click_interval = random.uniform(0.1, 2.0)  # Random click interval example
    total_clicks = 5  # Fixed number of clicks
    auto_clicker = AutoClicker(click_interval, total_clicks)
    auto_clicker.start_clicking()