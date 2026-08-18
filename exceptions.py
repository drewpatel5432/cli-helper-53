class InputValidationError(Exception):
    def __init__(self, message):
        super().__init__(message)

class ValueTooHighError(InputValidationError):
    def __init__(self, limit):
        super().__init__(f'Input value cannot exceed {limit}.')

class ValueTooLowError(InputValidationError):
    def __init__(self, limit):
        super().__init__(f'Input value cannot be less than {limit}.')

class InvalidInputTypeError(InputValidationError):
    def __init__(self, expected_type):
        super().__init__(f'Input must be of type {expected_type}.')


def validate_input(value, min_value, max_value):
    if not isinstance(value, (int, float)):
        raise InvalidInputTypeError('int or float')
    if value < min_value:
        raise ValueTooLowError(min_value)
    if value > max_value:
        raise ValueTooHighError(max_value)