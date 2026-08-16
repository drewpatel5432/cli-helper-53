import logging
import sys

def setup_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

def log_event(logger, event):
    logger.info(f'Event occurred: {event}')

if __name__ == '__main__':
    custom_logger = setup_logger('AutoClicker')
    log_event(custom_logger, 'Started clicker process')
    log_event(custom_logger, 'Performing click action')
    log_event(custom_logger, 'Stopped clicker process')