import re

def is_valid_click_position(position):
    if isinstance(position, tuple) and len(position) == 2:
        x, y = position
        return isinstance(x, int) and isinstance(y, int) and x >= 0 and y >= 0
    return False

def is_valid_click_interval(interval):
    return isinstance(interval, (int, float)) and interval > 0

def is_valid_hotkey(hotkey):
    valid_keys = {'ctrl', 'alt', 'shift', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10'}
    return hotkey in valid_keys or re.match(r'^[a-zA-Z]$', hotkey)

if __name__ == '__main__':
    print(is_valid_click_position((100, 200)))  # True
    print(is_valid_click_interval(0.5))           # True
    print(is_valid_hotkey('f5'))                   # True
    print(is_valid_hotkey('z'))                    # True
    print(is_valid_hotkey('invalid_key'))          # False
