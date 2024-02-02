import logging

logger = logging.getLogger(__name__)

def devide_number(dividend: int | float, divider: int | float):

    logger.debug('DEBUG log')
    logger.info('INFO log')
    logger.warning('WARNING log')
    logger.error('ERROR log')
    logger.critical('CRITICAL log')

    try:
        return dividend / divider
    except ZeroDivisionError:
        logger.exception('Произошло деление на 0')
