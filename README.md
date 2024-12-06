# Log Candy

Log Candy is a simple and colorful logging utility designed to make your debug messages more delightful and informative. It provides easy-to-use functions for logging messages with different levels of importance, using vibrant colors for better distinction.

## Features

- 🌈 **Color-Coded Logs**: Debug, Info, Warning, Error, and Result messages are each represented with a unique color for easy identification.

- 📝 **Readable Formatting**: Automatically formats multiline messages for improved readability.

- 🛠️ **Customizable Use**: Straightforward integration to be used anywhere in your Python projects.

## Installation

You can install `Log Candy` via `pip`:

```bash
pip install log-candy
```

## Requirements

- Python 3.11.4 or higher

The package may work with older versions of Python, but it has not been tested.

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

## Why Use Log Candy?

- 🛠 **Ease of Use**: No setup required, just import and start logging.

- 🌟 **Improved Clarity**: Quickly identify different types of logs by their color-coded format.

- 💡 **Multiline Support**: Automatically indents subsequent lines to keep your logs neat.

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