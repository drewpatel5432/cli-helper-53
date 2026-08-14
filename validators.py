import re

def validate_email(email: str) -> bool:
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None


def validate_positive_integer(value: int) -> bool:
    return isinstance(value, int) and value > 0


def validate_click_interval(interval: float) -> bool:
    return isinstance(interval, (int, float)) and interval >= 0.01


def validate_hotkey(hotkey: str) -> bool:
    allowed_keys = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'SPACE', 'ESC'}
    return hotkey in allowed_keys


def validate_click_duration(duration: float) -> bool:
    return isinstance(duration, (int, float)) and duration >= 0.0