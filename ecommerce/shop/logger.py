import logging
db_logger = logging.getLogger('db')

db_logger.info('[+]info message')
db_logger.warning('[!]warning message')

try:
    1/0
except Exception as e:
    db_logger.exception(e)
