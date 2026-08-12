import time
from threading import Thread, Event

class AutoClicker:
    def __init__(self, interval=0.1):
        self.interval = interval
        self._stop_event = Event()

    def click(self):
        # Simulate a mouse click
        print('Click!')

    def run(self):
        while not self._stop_event.is_set():
            self.click()
            time.sleep(self.interval)

    def start(self):
        self._thread = Thread(target=self.run)
        self._thread.start()

    def stop(self):
        self._stop_event.set()
        self._thread.join()

if __name__ == '__main__':
    autoclicker = AutoClicker(interval=0.05)
    try:
        autoclicker.start()
        time.sleep(5)
    finally:
        autoclicker.stop()