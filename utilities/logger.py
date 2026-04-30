from datetime import datetime
import inspect, logging

# Generate a timestamp for unique log file naming
now = datetime.now().strftime('%d%m%Y%H%M%S')


class Loggen:
    """
    Logger utility class for generating customized loggers for test automation.

    This class provides a static method to create a logger instance that writes
    detailed logs to a file. Each logger is named after the calling function
    for better traceability in test execution.

    Key Features:
    - Automatic log file creation with timestamp
    - Detailed log format including timestamp, level, logger name, function, line number, and message
    - DEBUG level logging for comprehensive information
    - File handler for persistent log storage

    Usage:
        log = Loggen.log_generator()
        log.info("This is an info message")
        log.error("This is an error message")
    """
    @staticmethod
    def log_generator():
        """
        Creates and configures a logger instance for the calling function.

        This method inspects the call stack to get the name of the calling function,
        creates a unique logger for it, and sets up file logging with a detailed format.

        Returns:
            logging.Logger: Configured logger instance ready for use

        Log Format:
            %(asctime)s | %(levelname)s | %(name)s | %(funcName)s | %(lineno)s | %(message)s

        Example Log Output:
            2023-12-01 10:30:45,123 | INFO | test_login | test_login | 25 | User login successful
        """
        # Get the name of the calling function using inspect
        log_name = inspect.stack()[1][3]

        # Create a logger with the function name
        logger = logging.getLogger(log_name)

        # Create a file handler for writing logs to file
        log_file = logging.FileHandler(f'./logs/credkart_logs.log')

        # Define the log message format
        log_format = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(funcName)s | %(lineno)s | %(message)s")

        # Apply the format to the file handler
        log_file.setFormatter(log_format)

        # Add the handler to the logger
        logger.addHandler(log_file)

        # Set the logging level to DEBUG to capture all levels of messages
        logger.setLevel(logging.DEBUG)

        # Return the configured logger
        return logger
