import logging
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='app.log', max_bytes=5*1024*1024, backup_count=5):
    logger = logging.getLogger('AutoClickerLogger')
    logger.setLevel(logging.DEBUG)
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

logger = setup_logger()  
logger.info('Logger is set up with rotation.')
logger.error('This is an error message')
logger.debug('Debug message for tracking')
logger.warning('Warning message')
logger.critical('Critical issue reported')