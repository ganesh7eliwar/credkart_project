from datetime import datetime
import logging
import inspect

now = datetime.now().strftime('%d%m%Y%H%M%S')

class Loggen:
    @staticmethod
    def log_generator():
        log_name = inspect.stack()[1][3]
        logger = logging.getLogger(log_name)
        log_file = logging.FileHandler(f'./logs/credkart_logs.log')
        log_format = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(funcName)s | %(lineno)s | %(message)s")
        log_file.setFormatter(log_format)
        logger.addHandler(log_file)
        logger.setLevel(logging.DEBUG)
        return logger
