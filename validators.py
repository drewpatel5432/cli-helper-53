import re

def validate_positive_integer(value):
    try:
        ivalue = int(value)
        if ivalue > 0:
            return True
        else:
            return False
    except ValueError:
        return False


def validate_float(value):
    try:
        fvalue = float(value)
        return True
    except ValueError:
        return False


def validate_click_interval(value):
    if validate_float(value):
        return float(value) > 0
    return False


def validate_click_count(value):
    return validate_positive_integer(value)  


if __name__ == '__main__':
    print(validate_positive_integer('5'))   # True
    print(validate_float('5.25'))            # True
    print(validate_click_interval('0.1'))    # True
    print(validate_click_count('3'))         # True
    print(validate_float('five'))             # False
    print(validate_click_interval('-1'))      # False
    print(validate_click_count('0'))          # False