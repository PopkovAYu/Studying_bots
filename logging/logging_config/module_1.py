import logging
from logging import LogRecord

from module_2 import devide_number
from module_3 import square_number

# Инициализируем логгер модуля
logger = logging.getLogger(__name__)

# Устанавливаем логгеру уровень DEBUG
logger.setLevel(logging.DEBUG)

# Определяем свой фильтр, наследуясь от класса Filter библиотеки logging
class ErrorLogFilter(logging.Filter):
    # Переопределяем метод filter, который принимает self и record
    # Переменная рекорд будет ссылаться на объект класса LogRecord
    def filter(self, record):
        return record.levelname == 'ERROR'

# Инициализируем форматтер
formatter_1 = logging.Formatter(
    fmt='[%(asctime)s] #%(levelname)-8s %(filename)s:'
        '%(lineno)d - %(name)s:%(funcName)s - %(message)s'
)

# Инмциализируем хэндлер, который будет записывать логи в файл 'error.log'
error_file = logging.FileHandler('error.log', 'w', encoding='utf-8')
# Устаанвливаем хэндлеру уровень DEBUG
error_file.setLevel(logging.DEBUG)

# Добавляем хэндлеру фильтр 'ErrorLogFilter', который будет пропускать в
# хэндлер только логи уровня 'ERROR'
error_file.addFilter(ErrorLogFilter())

# Определяем форматирование логов в хэндлере
error_file.setFormatter(formatter_1)

# Добавляем хэндлер в логгер
logger.addHandler(error_file)

def main():
    a, b = 12, 2
    c, d = 4, 0

    logger.debug('DEBUG log')
    logger.info('INFO log')
    logger.warning('WARNING log')
    logger.error('ERROR log')
    logger.critical('CRITICAL log')

    print(devide_number(a, square_number(b)))
    print(devide_number(square_number(c), d))
