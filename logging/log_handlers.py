import logging
import sys

format_1 = '#%(levelname)-8s [%(asctime)s] - %(filename)s:'\
           '%(lineno)d - %(name)s - %(message)s'
format_2 = '[{asctime}] #{levelname:8} {filename}:'\
           '{lineno} - {name} - {message}'

# First formatter:
formatter_1 = logging.Formatter(fmt=format_1)
# Second formatter
formatter_2 = logging.Formatter(
    fmt=format_2,
    style='{'
)

# Creating logger
logger = logging.getLogger(__name__)


# Handler for stderr
stderr_handler = logging.StreamHandler()
# Handler for stdout
stdout_handler = logging.StreamHandler(sys.stdout)

# Formatters for handlers
stderr_handler.setFormatter(formatter_1)
stdout_handler.setFormatter(formatter_2)

# Adding handlers to logger
logger.addHandler(stdout_handler)
logger.addHandler(stderr_handler)

logger.warning('This is warning log')
