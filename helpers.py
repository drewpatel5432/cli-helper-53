import time
from typing import Callable, Any

def validate_input(user_input: str, valid_options: list) -> bool:
    return user_input in valid_options


def autoclicker_loop(click_function: Callable[[Any], None], options: list):
    while True:
        user_input = input('Enter command (start/stop): ').strip().lower()
        if not validate_input(user_input, options):
            print('Invalid command! Please use one of the following:', options)
            continue
        if user_input == 'start':
            print('Autoclicker started!')
            while True:
                click_function()
                time.sleep(1)  # Simulate click interval
        elif user_input == 'stop':
            print('Autoclicker stopped!')
            break


if __name__ == '__main__':
    autoclicker_loop(lambda: print('Clicked!'), ['start', 'stop'])