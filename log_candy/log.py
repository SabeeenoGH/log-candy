import json
from typing import Any

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

# Formatting configuration
_compact_objects = True  # Set to False for indented formatting like before
_compact_threshold = 100  # Objects longer than this use minimal spacing even if compact_objects=False

def set_compact_formatting(enabled: bool = True, threshold: int = 100) -> None:
    '''Configure object formatting for logging
    
    Args:
        enabled (bool): If True, use compact formatting for all objects.
                       If False, use indented formatting for readability.
        threshold (int): For non-compact mode, objects longer than this threshold
                        will still use compact formatting to avoid excessive output.
    '''
    global _compact_objects, _compact_threshold
    _compact_objects = enabled
    _compact_threshold = threshold

def get_formatting_settings() -> dict:
    '''Get current formatting settings
    
    Returns:
        dict: Current formatting configuration
    '''
    return {
        'compact_objects': _compact_objects,
        'compact_threshold': _compact_threshold
    }

def _format_message(message: Any) -> str:
    '''Convert any object to a formatted string for logging
    
    Args:
        message: The object to format
        
    Returns:
        str: The formatted string representation
    '''
    if isinstance(message, str):
        return message
    elif isinstance(message, (dict, list, tuple, set)):
        try:
            if _compact_objects:
                # Always use compact formatting
                return json.dumps(message, ensure_ascii=False, default=str, separators=(',', ':'))
            else:
                # Use indented formatting, but check threshold for very long objects
                compact = json.dumps(message, ensure_ascii=False, default=str, separators=(',', ':'))
                if len(compact) > _compact_threshold:
                    # Object is too long, use minimal spacing for readability
                    return json.dumps(message, ensure_ascii=False, default=str, separators=(',', ': '))
                else:
                    # Object is reasonable size, use full indentation
                    return json.dumps(message, indent=2, ensure_ascii=False, default=str)
        except (TypeError, ValueError):
            return str(message)
    else:
        return str(message)

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

def log_debug(message: Any) -> None:
    '''Print a debug message

    Args:
        message: The message to print (can be any object type)
    '''
    if not _should_log('DEBUG'):
        return

    # Convert message to string
    formatted_message = _format_message(message)
    
    # Replace newlines with newlines and spaces
    formatted_message = formatted_message.replace("\n", "\n" + " " * len('[DEBUG] '))

    # Print the message
    print(f"{log_candy.DEBUG}[DEBUG] {formatted_message}{log_candy.ENDC}")

def log_info(message: Any) -> None:
    '''Print an info message

    Args:
        message: The message to print (can be any object type)
    '''
    if not _should_log('INFO'):
        return

    # Convert message to string
    formatted_message = _format_message(message)
    
    # Replace newlines with newlines and spaces
    formatted_message = formatted_message.replace("\n", "\n" + " " * len('[INFO] '))

    # Print the message
    print(f"{log_candy.INFO}[INFO] {formatted_message}{log_candy.ENDC}")

def log_result(message: Any) -> None:
    '''Print a result message

    Args:
        message: The message to print (can be any object type)
    '''
    if not _should_log('RESULT'):
        return
    
    # Convert message to string
    formatted_message = _format_message(message)
    
    # Replace newlines with newlines and spaces
    formatted_message = formatted_message.replace("\n", "\n" + " " * len('[RESULT] '))

    # Print the message
    print(f"{log_candy.RESULT}[RESULT] {formatted_message}{log_candy.ENDC}")

def log_warning(message: Any) -> None:
    '''Print a warning message

    Args:
        message: The message to print (can be any object type)
    '''
    if not _should_log('WARNING'):
        return

    # Convert message to string
    formatted_message = _format_message(message)
    
    # Replace newlines with newlines and spaces
    formatted_message = formatted_message.replace("\n", "\n" + " " * len('[WARNING] '))

    # Print the message
    print(f"{log_candy.WARNING}[WARNING] {formatted_message}{log_candy.ENDC}")

def log_error(message: Any) -> None:
    '''Print an error message

    Args:
        message: The message to print (can be any object type)
    '''
    if not _should_log('ERROR'):
        return

    # Convert message to string
    formatted_message = _format_message(message)
    
    # Replace newlines with newlines and spaces
    formatted_message = formatted_message.replace("\n", "\n" + " " * len('[ERROR] '))

    # Print the message
    print(f"{log_candy.ERROR}[ERROR] {formatted_message}{log_candy.ENDC}")

def tqdm_info(message: Any) -> str:
    '''Return an info message for tqdm

    Args:
        message: The message to return (can be any object type)

    Returns:
        str: The formatted message
    '''
    # Convert message to string
    formatted_message = _format_message(message)
    
    return f"{log_candy.INFO}[INFO] {formatted_message}"

def input_debug(message: Any) -> str:
    '''Return an input message for debugging

    Args:
        message: The message to display (can be any object type)

    Returns:
        str: The user input
    '''
    # Convert message to string
    formatted_message = _format_message(message)
    
    return input(f"{log_candy.DEBUG}[INPUT DEBUG] {formatted_message}{log_candy.ENDC}")

