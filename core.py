import time
import threading

class AutoClicker:
    def __init__(self, interval=1.0):
        self.interval = interval
        self._running = threading.Event()
        self._click_thread = None

    def start(self):
        if not self._running.is_set():
            self._running.set()
            self._click_thread = threading.Thread(target=self._click)
            self._click_thread.start()

    def stop(self):
        self._running.clear()
        if self._click_thread:
            self._click_thread.join()
            self._click_thread = None

    def _click(self):
        while self._running.is_set():
            self.perform_click()
            time.sleep(self.interval)

    def perform_click(self):
        print("Click!")  # Simulating a click action

if __name__ == '__main__':
    clicker = AutoClicker(interval=0.5)
    clicker.start()
    time.sleep(5)  # Run for 5 seconds
    clicker.stop()