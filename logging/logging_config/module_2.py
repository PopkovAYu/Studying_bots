import logging
from logging import LogRecord
import sys

# Инициализируем логгер модуля
logger = logging.getLogger(__name__)

# Определяем свой фильтр, наследуясь от класса Filter библиотеки logging
class DebugWarningLogFilter(logging.Filter):
    # Переопределяем метод filter, который принимает self и record
    # Переменная record будет ссылаться на объект LogRecord
    def filter(self, record):
        return record.levelname in ('DEBUG', 'WARNING')

# Инициализируем форматтер
formatter_2 = logging.Formatter(
    fmt='[%(asctime)s] #%(levelname)-8s %(filename)s:'
        '%(lineno)d - %(name)s:%(funcName)s - %(message)s'
)

# Инициализируем хэндлер, который будет писать логи в stdout
stdout = logging.StreamHandler(sys.stdout)

# Добавляем хэндлеру фильтр 'DebugWarningLogFilter', который будет пропускать в
# хэндлер только логи уровня DEBUG и WARNING
stdout.addFilter(DebugWarningLogFilter())

# Определяем форматирование логов в хэндлере
stdout.setFormatter(formatter_2)

# Добавляем хэндлер к логгеру
logger.addHandler(stdout)

def devide_number(dividend: int | float, devider: int | float):

    logger.debug('DEBUG log')
    logger.info('INFO log')
    logger.warning('WARNING log')
    logger.error('ERROR log')
    logger.critical('CRITICAL log')

    try:
        return dividend / devider
    except ZeroDivisionError:
        logger.exception('Произошло деление на 0')
