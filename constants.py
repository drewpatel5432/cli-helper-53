import os

# Mouse click settings
CLICK_DELAY = 0.1  # Delay between clicks in seconds
MAX_CLICKS = 1000  # Maximum number of clicks

# Hotkey settings
HOTKEY_START = 'ctrl+shift+s'
HOTKEY_STOP = 'ctrl+shift+x'

# File paths
LOG_FILE = os.path.join(os.getcwd(), 'autoclicker.log')
CONFIG_FILE = os.path.join(os.getcwd(), 'config.json')

# Screen dimensions
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# Mouse button options
LEFT_BUTTON = 1
RIGHT_BUTTON = 2
MIDDLE_BUTTON = 3

# Status messages
STATUS_RUNNING = 'Autoclicker is running'
STATUS_STOPPED = 'Autoclicker is stopped'
STATUS_ERROR = 'An error has occurred'

# Other constants
VERSION = '1.0.0'
DEVELOPER_NAME = 'cli-helper-53'