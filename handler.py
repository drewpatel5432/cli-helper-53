import time
import sys

class AutoClicker:
    def __init__(self, delay):
        self.delay = delay

    def start_clicking(self):
        print("AutoClicker started. Press Ctrl+C to stop.")
        try:
            while True:
                self.perform_click()
                time.sleep(self.delay)
        except KeyboardInterrupt:
            print("AutoClicker stopped.")

    def perform_click(self):
        print("Click!")

def validate_input(user_input):
    try:
        value = float(user_input)
        if value < 0:
            raise ValueError("Delay must be a positive number.")
        return value
    except ValueError as e:
        print(f'Invalid input: {e}')
        sys.exit(1)

if __name__ == '__main__':
    user_input = input("Enter delay in seconds: ")
    validated_delay = validate_input(user_input)
    auto_clicker = AutoClicker(validated_delay)
    auto_clicker.start_clicking()