import logging
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='app.log', max_size=5 * 1024 * 1024, backup_count=3):
    logger = logging.getLogger('AutoClicker')
    logger.setLevel(logging.DEBUG)

    handler = RotatingFileHandler(log_file, maxBytes=max_size, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger

# Example usage
if __name__ == '__main__':
    logger = setup_logger()
    logger.info('Logger setup complete.')
    logger.debug('This is a debug message.')
    logger.warning('This is a warning message.')
    logger.error('This is an error message.')
    logger.critical('This is a critical message.')