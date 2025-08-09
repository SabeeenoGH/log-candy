class log_candy:
    DEBUG = '\033[95m'
    INFO = '\033[94m'
    RESULT = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    ENDC = '\033[0m'

# Log levels hierarchy (lower number = higher priority)
LOG_LEVELS = {
    'DEBUG': 10,
    'INFO': 20,
    'RESULT': 25,
    'WARNING': 30,
    'ERROR': 40
}

# Current log level (default to DEBUG to show all logs)
_current_log_level = LOG_LEVELS['DEBUG']

def set_log_level(level: str) -> None:
    '''Set the minimum log level to display

    Args:
        level (str): The log level ('DEBUG', 'INFO', 'RESULT', 'WARNING', 'ERROR')
    '''
    global _current_log_level
    level = level.upper()
    if level in LOG_LEVELS:
        _current_log_level = LOG_LEVELS[level]
    else:
        raise ValueError(f"Invalid log level: {level}. Valid levels are: {', '.join(LOG_LEVELS.keys())}")

def get_log_level() -> str:
    '''Get the current log level

    Returns:
        str: The current log level as a string
    '''
    for level_name, level_value in LOG_LEVELS.items():
        if level_value == _current_log_level:
            return level_name
    return 'DEBUG'

def _should_log(level: str) -> bool:
    '''Check if a message with the given level should be logged

    Returns:
        bool: True if the message should be logged, False otherwise
    '''
    return LOG_LEVELS[level] >= _current_log_level    

def log_debug(message: str) -> None:
    '''Print a debug message

    Args:
        message (str): The message to print
    '''
    if not _should_log('DEBUG'):
        return

    # Replace newlines with newlines and spaces
    message = message.replace("\n", "\n" + " " * len('[DEBUG] '))

    # Print the message
    print(f"{log_candy.DEBUG}[DEBUG] {message}{log_candy.ENDC}")

def log_info(message: str) -> None:
    '''Print an info message

    Args:
        message (str): The message to print
    '''
    if not _should_log('INFO'):
        return

    # Replace newlines with newlines and spaces
    message = message.replace("\n", "\n" + " " * len('[INFO] '))

    # Print the message
    print(f"{log_candy.INFO}[INFO] {message}{log_candy.ENDC}")

def log_result(message: str) -> None:
    '''Print a result message

    Args:
        message (str): The message to print
    '''
    if not _should_log('RESULT'):
        return
    
    # Replace newlines with newlines and spaces
    message = message.replace("\n", "\n" + " " * len('[RESULT] '))

    # Print the message
    print(f"{log_candy.RESULT}[RESULT] {message}{log_candy.ENDC}")

def log_warning(message: str) -> None:
    '''Print a warning message

    Args:
        message (str): The message to print
    '''
    if not _should_log('WARNING'):
        return

    # Replace newlines with newlines and spaces
    message = message.replace("\n", "\n" + " " * len('[WARNING] '))

    # Print the message
    print(f"{log_candy.WARNING}[WARNING] {message}{log_candy.ENDC}")

def log_error(message: str) -> None:
    '''Print an error message

    Args:
        message (str): The message to print
    '''
    if not _should_log('ERROR'):
        return

    # Replace newlines with newlines and spaces
    message = message.replace("\n", "\n" + " " * len('[ERROR] '))

    # Print the message
    print(f"{log_candy.ERROR}[ERROR] {message}{log_candy.ENDC}")

def tqdm_info(message: str) -> str:
    '''Return an info message for tqdm

    Args:
        message (str): The message to return

    Returns:
        str: The formatted message
    '''

    return f"{log_candy.INFO}[INFO] {message}"

def input_debug(message: str) -> str:
    '''Return an input message for debugging

    Args:
        message (str): The message to return

    Returns:
        str: The formatted message
    '''
    
    return input(f"{log_candy.DEBUG}[INPUT DEBUG] {message}{log_candy.ENDC}")

