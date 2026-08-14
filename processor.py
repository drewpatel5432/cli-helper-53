import time
import pyautogui

class AutoClicker:
    def __init__(self, interval=0.1):
        self.interval = interval
        self.running = False

    def start_clicking(self):
        self.running = True
        print("AutoClicker started.")
        while self.running:
            pyautogui.click()
            time.sleep(self.interval)

    def stop_clicking(self):
        self.running = False
        print("AutoClicker stopped.")

    def set_interval(self, interval):
        if interval <= 0:
            raise ValueError("Interval must be a positive number.")
        self.interval = interval

if __name__ == '__main__':
    clicker = AutoClicker(0.1)
    try:
        clicker.start_clicking()
    except KeyboardInterrupt:
        clicker.stop_clicking()