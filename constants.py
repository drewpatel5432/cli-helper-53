import time

DEFAULT_RETRY_COUNT = 3
DEFAULT_BACKOFF_FACTOR = 0.5

class RetryConfig:
    def __init__(self, max_retries=DEFAULT_RETRY_COUNT, backoff_factor=DEFAULT_BACKOFF_FACTOR):
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor

    def calculate_backoff_time(self, attempt):
        return self.backoff_factor * (2 ** (attempt - 1))

retry_config = RetryConfig()