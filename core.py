import time
import threading

class AutoClicker:
    def __init__(self, interval=0.1):
        self.interval = interval
        self.running = False
        self.click_thread = None

    def _click(self):
        while self.running:
            print("Click!")  # Simulated click action
            time.sleep(self.interval)

    def start(self):
        if not self.running:
            self.running = True
            self.click_thread = threading.Thread(target=self._click)
            self.click_thread.start()

    def stop(self):
        if self.running:
            self.running = False
            self.click_thread.join()

if __name__ == '__main__':
    autoclicker = AutoClicker(interval=0.05)
    autoclicker.start()
    time.sleep(1)
    autoclicker.stop()