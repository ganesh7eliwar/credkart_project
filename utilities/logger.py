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

        How it works:
            1. Uses Python's inspect module to extract the calling function name from the stack
            2. Creates a logger instance with the function name as identifier
            3. Configures file handler to write to ./logs/credkart_logs.log
            4. Applies a detailed log format including timestamp, level, and line number
            5. Sets logging level to DEBUG (lowest level) to capture all message types

        Returns:
            logging.Logger: Configured logger instance ready for use

        Log Format:
            %(asctime)s | %(levelname)s | %(name)s | %(funcName)s | %(lineno)s | %(message)s

        Explanation of format fields:
            - %(asctime)s: Timestamp when log entry was created (e.g., 2023-12-01 10:30:45,123)
            - %(levelname)s: Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
            - %(name)s: Logger name (set to calling function name by this method)
            - %(funcName)s: Name of the function that created the log entry
            - %(lineno)s: Line number in the source code where log was called
            - %(message)s: The actual log message

        Example Log Output:
            2023-12-01 10:30:45,123 | INFO | test_login | test_login | 25 | User login successful

        Note:
            - Multiple loggers write to the same file (credkart_logs.log)
            - Each test maintains its own logger instance but shares the log file
            - Log file persists between test runs (appends new entries)
        """

        # STEP 1: Extract the calling function's name from the call stack
        # inspect.stack()[1] gets the immediate caller's frame
        # inspect.stack()[1][3] extracts the function name from that frame
        log_name = inspect.stack()[1][3]

        # STEP 2: Create a logger instance with the extracted function name
        # If logger with this name already exists, get existing instance (singleton pattern)
        logger = logging.getLogger(log_name)

        # STEP 3: Create a file handler that appends logs to the specified file path
        # './logs/credkart_logs.log' - All loggers write to this central file
        # FileHandler(mode='a') - Append mode (default) - doesn't overwrite existing logs
        log_file = logging.FileHandler(f'./logs/credkart_logs.log')

        # STEP 4: Define the log message format with all available metadata
        # This format makes each log entry highly informative and traceable
        log_format = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(funcName)s | %(lineno)s | %(message)s"
        )

        # STEP 5: Apply the defined format to the file handler
        # This ensures all log entries written by this handler follow the format
        log_file.setFormatter(log_format)

        # STEP 6: Attach the configured file handler to the logger
        # A logger can have multiple handlers (file, console, etc.)
        # We only use file handler for persistent storage
        logger.addHandler(log_file)

        # STEP 7: Set the logging level to DEBUG (lowest level)
        # DEBUG < INFO < WARNING < ERROR < CRITICAL
        # Setting to DEBUG ensures all message levels are captured
        logger.setLevel(logging.DEBUG)

        # STEP 8: Return the fully configured logger instance
        # The caller can now use log.info(), log.warning(), log.error(), etc.
        return logger
