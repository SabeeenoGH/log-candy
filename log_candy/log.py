class log_candy:
    DEBUG = '\033[95m'
    INFO = '\033[94m'
    RESULT = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    ENDC = '\033[0m'    

def log_debug(message: str) -> None:
    '''
    Print a debug message

    :param message: The message to print
    '''

    # Replace newlines with newlines and spaces
    message = message.replace("\n", "\n" + " " * len('[DEBUG] '))

    # Print the message
    print(f"{log_candy.DEBUG}[DEBUG] {message}{log_candy.ENDC}")

def log_info(message: str) -> None:
    '''
    Print an info message

    :param message: The message to print
    '''

    # Replace newlines with newlines and spaces
    message = message.replace("\n", "\n" + " " * len('[INFO] '))

    # Print the message
    print(f"{log_candy.INFO}[INFO] {message}{log_candy.ENDC}")

def log_result(message: str) -> None:
    '''
    Print a result message

    :param message: The message to print
    '''
    
    # Replace newlines with newlines and spaces
    message = message.replace("\n", "\n" + " " * len('[RESULT] '))

    # Print the message
    print(f"{log_candy.RESULT}[RESULT] {message}{log_candy.ENDC}")

def log_warning(message: str) -> None:
    '''
    Print a warning message

    :param message: The message to print
    '''

    # Replace newlines with newlines and spaces
    message = message.replace("\n", "\n" + " " * len('[WARNING] '))

    # Print the message
    print(f"{log_candy.WARNING}[WARNING] {message}{log_candy.ENDC}")

def log_error(message: str) -> None:
    '''
    Print an error message
    
    :param message: The message to print
    '''

    # Replace newlines with newlines and spaces
    message = message.replace("\n", "\n" + " " * len('[ERROR] '))

    # Print the message
    print(f"{log_candy.ERROR}[ERROR] {message}{log_candy.ENDC}")

def tqdm_info(message: str) -> str:
    '''
    Return an info message for tqdm

    :param message: The message to return
    :return: The formatted message
    '''

    return f"{log_candy.INFO}[INFO] {message}"

def input_debug(message: str) -> str:
    '''
    Return an input message for debugging

    :param message: The message to return
    :return: The formatted message
    '''
    
    return input(f"{log_candy.DEBUG}[INPUT DEBUG] {message}{log_candy.ENDC}")

