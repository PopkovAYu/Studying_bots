import logging
from logging import LogRecord

# Difining filter
class ErrorLogFilter(logging.Filter):
    def filter(self, record):
        return record.levelname == 'ERROR' and 'важно' in record.msg.lower()

# Initializing logger
logger = logging.getLogger(__name__)

# Creating handler - logs to stderr
stderr_handler = logging.StreamHandler()

# Connect filter to handler
stderr_handler.addFilter(ErrorLogFilter())

# Connect handler to logger
logger.addHandler(stderr_handler)

logger.warning('Важно! Это лог  спредупреждением')
logger.error('Важно! Это лог с ошибкой')
logger.info('Важно! Это лог уровня INFO')
logger.error('Это лог с ошибкой')