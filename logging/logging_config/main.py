import logging

from module_1 import main

# Base config tuning
logging.basicConfig(
    format='#%(levelname)-8s %(name)s:%(funcName)s - %(message)s'
)

# Executing main function from module_1
main()
