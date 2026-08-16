import logging
import time
import json
from typing import Callable, Any

def setup_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

logger = setup_logger('retry_logger')

def retry(func: Callable, retries: int = 3, delay: int = 2, *args: Any, **kwargs: Any) -> Any:
    for attempt in range(retries):
        try:
            logger.debug(f'Attempt {attempt + 1} for function {func.__name__}')
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f'Attempt {attempt + 1} failed: {e}')
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                logger.critical('Maximum retries reached')
                raise
