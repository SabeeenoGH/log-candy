# Log Candy

Log Candy is a simple and colorful logging utility designed to make your debug messages more delightful and informative. It provides easy-to-use functions for logging messages with different levels of importance, using vibrant colors for better distinction.

## Features

- 🌈 **Color-Coded Logs**: Debug, Info, Warning, Error, and Result messages are each represented with a unique color for easy identification.

- 📝 **Readable Formatting**: Automatically formats multiline messages for improved readability.

- 🎚️ **Log Level Control**: Set minimum log levels to filter out less important messages and reduce noise.

- 🛠️ **Customizable Use**: Straightforward integration to be used anywhere in your Python projects.

## Installation

You can install `Log Candy` via `pip`:

```bash
pip install log-candy
```

## Requirements

- Python 3 version or higher is required.

## Dependencies

The package also carries the following dependencies (`requirements.txt`) for better use:

```bash
tqdm==4.66.4
```

## Usage

Import `Log Candy` and start logging colorful messages in your project:

```python
from log_candy import log_debug, log_info, log_warning, log_error, log_result

# Classic logging
log_debug("This is a debug message.")
log_info("This is an info message.")
log_warning("This is a warning message.")
log_error("This is an error message.")
log_result("This is a result message.")

# Multiline logging
log_debug("This is a debug message.\nThis is a multiline debug message.")
log_info("This is an info message.\nThis is a multiline info message.")
log_warning("This is a warning message.\nThis is a multiline warning message.")
log_error("This is an error message.\nThis is a multiline error message.")
log_result("This is a result message.\nThis is a multiline result message.")
```

### Log Levels

You can control which logs are displayed by setting a minimum log level. Only logs at or above the set level will be shown:

```python
from log_candy import set_log_level, get_log_level, LOG_LEVELS

# Set log level to show only warnings and errors
set_log_level('WARNING')

log_debug("This won't be shown")        # Hidden
log_info("This won't be shown")         # Hidden
log_warning("This will be shown")       # Visible
log_error("This will be shown")         # Visible

# Check current log level
current_level = get_log_level()
print(f"Current log level: {current_level}")

# Available log levels (in order of priority):
# DEBUG (10) - Shows all logs
# INFO (20) - Shows info, result, warning, and error logs
# RESULT (25) - Shows result, warning, and error logs  
# WARNING (30) - Shows warning and error logs
# ERROR (40) - Shows only error logs

# You can also access the LOG_LEVELS dictionary
print("Available levels:", LOG_LEVELS)
```

## Why Use Log Candy?

- 🛠 **Ease of Use**: No setup required, just import and start logging.

- 🌟 **Improved Clarity**: Quickly identify different types of logs by their color-coded format.

- 💡 **Multiline Support**: Automatically indents subsequent lines to keep your logs neat.

- 🎯 **Focused Debugging**: Use log levels to show only the information you need, when you need it.

## Contributing

Contributions are welcome! If you have suggestions for improvements, please feel free to open an issue or create a pull request.

### Steps to Contribute

1. Fork the repository.

2. Create a new branch (`git checkout -b feature/amazing-feature`).

3. Commit your changes (`git commit -m 'Add amazing feature'`).

4. Push to the branch (`git push origin feature/amazing-feature`).

5. Open a Pull Request.

## Acknowledgements

Special thanks to anyone who finds this project useful and helps make it better!

Enjoy logging with Log Candy 🍭!