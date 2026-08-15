def validate_click_interval(interval):
    if not isinstance(interval, (int, float)):
        raise ValueError("Interval must be a number.")
    if interval <= 0:
        raise ValueError("Interval must be greater than zero.")
    return True


def validate_click_count(count):
    if not isinstance(count, int):
        raise ValueError("Click count must be an integer.")
    if count < 1:
        raise ValueError("Click count must be at least 1.")
    return True


def validate_mouse_buttons(buttons):
    valid_buttons = {'left', 'right', 'middle'}
    if not all(button in valid_buttons for button in buttons):
        raise ValueError(f"Invalid mouse button(s) provided: {buttons}")
    return True


def validate_configuration(config):
    try:
        validate_click_interval(config.get('click_interval', 0))
        validate_click_count(config.get('click_count', 1))
        validate_mouse_buttons(config.get('mouse_buttons', ['left']))
    except ValueError as e:
        raise ValueError(f"Configuration error: {e}") from e
    return True