# 🍭 Log Candy

[![PyPI version](https://badge.fury.io/py/log-candy.svg)](https://badge.fury.io/py/log-candy)
[![Python version](https://img.shields.io/pypi/pyversions/log-candy.svg)](https://pypi.org/project/log-candy/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Log Candy** is a delightful and powerful Python logging utility that transforms your debugging experience with colorful, well-formatted terminal output. Whether you're debugging complex data structures, monitoring application flow, or building interactive tools, Log Candy makes your logs both beautiful and informative.

## ✨ Features

- 🌈 **5 Color-Coded Log Levels**: Each log type has its distinct color for instant visual recognition
- 🎯 **Universal Object Support**: Log strings, numbers, lists, dictionaries, custom objects - anything!
- 🎚️ **Smart Log Level Filtering**: Show only the logs you need with configurable minimum levels
- 🎨 **Flexible Formatting Options**: Choose between compact and indented formatting for complex objects
- 📊 **Progress Bar Integration**: Built-in support for tqdm-style progress indicators
- � **Interactive Debugging**: Special input functions for interactive debugging sessions
- 📝 **Multiline Support**: Automatically handles and properly indents multiline messages
- 🚀 **Zero Configuration**: Works out of the box - just import and start logging
- ⚡ **High Performance**: Minimal overhead with intelligent formatting thresholds

## 🚀 Quick Start

### Installation

Install Log Candy via pip:

```bash
pip install log-candy
```

### Basic Usage

```python
from log_candy import log_debug, log_info, log_result, log_warning, log_error

# Simple string logging
log_debug("🔧 Debugging application startup")
log_info("📋 Processing user data") 
log_result("✅ Operation completed successfully")
log_warning("⚠️ Low disk space detected")
log_error("❌ Failed to connect to database")
```

### Try a Quick Test

Create your own quick test to see Log Candy in action:

```python
from log_candy import *

# Test different object types
log_info("Hello, Log Candy! 🍭")
log_debug({"user": "Alice", "score": 95, "active": True})
log_result([1, 2, 3, "success", {"nested": "data"}])

# Control what you see
set_log_level('INFO')  # Hide debug messages
log_debug("This won't show")
log_info("This will show!")
```

## 📚 Comprehensive Usage Guide

### Log Levels & Colors

Log Candy provides 5 distinct log levels, each with its own color and purpose:

| Level | Color | Function | Use Case |
|-------|--------|----------|----------|
| 🟣 **DEBUG** | Purple | `log_debug()` | Development debugging, detailed tracing |
| 🔵 **INFO** | Blue | `log_info()` | General information, application flow |
| 🟢 **RESULT** | Green | `log_result()` | Important outcomes, successful operations |
| 🟡 **WARNING** | Yellow | `log_warning()` | Potential issues, non-critical problems |
| 🔴 **ERROR** | Red | `log_error()` | Critical errors, failures requiring attention |

```python
from log_candy import *

# All log levels in action
log_debug("🔍 Inspecting variable state before processing")
log_info("📊 Starting data analysis pipeline") 
log_result("🎯 Analysis complete: 1,234 records processed")
log_warning("⚠️ Memory usage is high (85%)")
log_error("💥 Database connection failed after 3 retries")
```

### Object Type Support

Log Candy intelligently handles any Python object type:

```python
# Primitive types
log_info("Simple string message")
log_debug(42)                          # Numbers
log_result(3.14159)                    # Floats
log_warning(True)                      # Booleans
log_info(None)                         # None values

# Collections (auto-formatted as JSON)
log_info([1, 2, 3, "test", True])                    # Lists
log_debug({"name": "Alice", "age": 30, "active": True})  # Dictionaries
log_result((10.5, 20.3, "coordinates"))              # Tuples
log_warning({1, 2, 3, 4, 5})                        # Sets

# Complex nested structures
user_profile = {
    "id": 12345,
    "personal": {
        "name": "Alice Johnson",
        "email": "alice@example.com",
        "preferences": {
            "theme": "dark",
            "notifications": True,
            "language": "en"
        }
    },
    "activity": {
        "last_login": "2025-08-09T10:30:00Z",
        "sessions": [
            {"date": "2025-08-09", "duration": 45},
            {"date": "2025-08-08", "duration": 32}
        ]
    }
}
log_debug(user_profile)  # Beautifully formatted JSON

# Custom objects
class Product:
    def __init__(self, name, price, in_stock=True):
        self.name = name
        self.price = price
        self.in_stock = in_stock
    
    def __str__(self):
        return f"Product(name='{self.name}', price=${self.price}, in_stock={self.in_stock})"

product = Product("MacBook Pro", 2399.99, True)
log_info(product)  # Uses the __str__ method

# Even works with multiline content
multiline_data = """Configuration loaded:
- Database: PostgreSQL
- Cache: Redis  
- Queue: RabbitMQ
- Environment: Production"""
log_result(multiline_data)  # Properly indented output
```

### Smart Log Level Control

Control which messages are displayed by setting a minimum log level. This is perfect for different environments (development vs production):

```python
from log_candy import set_log_level, get_log_level, LOG_LEVELS

# Show all messages (default)
set_log_level('DEBUG')
log_debug("🔧 Detailed debugging info")     # ✅ Visible
log_info("📊 General information")          # ✅ Visible  
log_warning("⚠️ Something to watch")        # ✅ Visible

# Production mode - show only important messages
set_log_level('WARNING') 
log_debug("🔧 Debug details")               # ❌ Hidden
log_info("📊 Process started")              # ❌ Hidden
log_warning("⚠️ High memory usage")         # ✅ Visible
log_error("💥 Critical failure")            # ✅ Visible

# Check current setting
current_level = get_log_level()
log_info(f"Current log level: {current_level}")

# Available levels (in priority order):
print("📊 Available log levels:", LOG_LEVELS)
# Output: {'DEBUG': 10, 'INFO': 20, 'RESULT': 25, 'WARNING': 30, 'ERROR': 40}
```

### Advanced Formatting Control

Control how complex objects are formatted for optimal readability:

```python
from log_candy import set_compact_formatting, get_formatting_settings

# Example complex object
server_config = {
    "database": {
        "hosts": ["db1.example.com", "db2.example.com"],
        "credentials": {"user": "app_user", "password": "***"},
        "pool_size": 20
    },
    "cache": {"redis_url": "redis://cache.example.com:6379", "ttl": 3600},
    "monitoring": {"enabled": True, "endpoints": ["/health", "/metrics"]}
}

# Compact formatting (default) - single line
set_compact_formatting(enabled=True)
log_debug(server_config)
# Output: {"database":{"hosts":["db1.example.com","db2.example.com"]...}

# Indented formatting for readability
set_compact_formatting(enabled=False, threshold=100)
log_debug(server_config)
# Output: 
# {
#   "database": {
#     "hosts": [
#       "db1.example.com", 
#       "db2.example.com"
#     ],
#     ...
#   }
# }

# Hybrid approach - compact for small objects, indented for large ones
set_compact_formatting(enabled=False, threshold=50)
small_obj = {"status": "ok", "count": 5}
log_info(small_obj)  # Compact format (under threshold)
log_info(server_config)  # Indented format (over threshold)

# Check current settings
settings = get_formatting_settings()
log_debug(f"📋 Current formatting: {settings}")
```

### Special Functions for Advanced Use Cases

#### Progress Bar Integration

Perfect for monitoring long-running operations:

```python
from log_candy import tqdm_info
import time

# Simulate a progress bar
total_items = 100
for i in range(total_items):
    # Your processing logic here
    time.sleep(0.01)  
    
    # Update progress with colored message
    progress_msg = tqdm_info(f"Processing item {i+1}/{total_items} ({((i+1)/total_items)*100:.1f}%)")
    print(f"\r{progress_msg}", end="", flush=True)

print()  # New line when complete
log_result("✅ Processing completed!")
```

#### Interactive Debugging

For interactive debugging sessions:

```python
from log_candy import input_debug

# Interactive debugging with colored prompts
user_name = input_debug("👤 Enter your name for testing: ")
user_age = input_debug(f"🎂 Enter age for {user_name}: ")

log_result(f"✅ Test user created: {user_name}, age {user_age}")

# Debug complex objects interactively
debug_data = {"name": user_name, "age": int(user_age), "test_session": True}
confirm = input_debug(f"🔍 Debug this data? {debug_data} (y/n): ")

if confirm.lower() == 'y':
    log_debug(debug_data)
```

## 🎯 Real-World Use Cases

### Web Application Debugging

```python
from log_candy import *

# API endpoint logging
@app.route('/api/users/<user_id>')
def get_user(user_id):
    log_info(f"🌐 API Request: GET /api/users/{user_id}")
    
    try:
        # Database query
        user_data = database.get_user(user_id)
        log_debug(f"📊 Query result: {user_data}")
        
        if user_data:
            log_result(f"✅ User found: {user_data['name']}")
            return jsonify(user_data)
        else:
            log_warning(f"⚠️ User not found: {user_id}")
            return jsonify({"error": "User not found"}), 404
            
    except Exception as e:
        log_error(f"💥 Database error: {e}")
        return jsonify({"error": "Internal server error"}), 500
```

### Data Science Pipeline

```python
import pandas as pd
from log_candy import *

def analyze_dataset(file_path):
    set_log_level('INFO')  # Hide debug in production
    
    log_info(f"📁 Loading dataset: {file_path}")
    df = pd.read_csv(file_path)
    
    # Data exploration
    dataset_info = {
        "rows": len(df),
        "columns": len(df.columns),
        "memory_usage": f"{df.memory_usage(deep=True).sum() / 1024**2:.2f} MB",
        "null_values": df.isnull().sum().sum()
    }
    log_debug(dataset_info)
    
    if dataset_info["null_values"] > 0:
        log_warning(f"⚠️ Found {dataset_info['null_values']} null values")
    
    # Analysis results
    results = {
        "mean_age": df['age'].mean(),
        "total_revenue": df['revenue'].sum(),
        "top_categories": df['category'].value_counts().head(3).to_dict()
    }
    log_result(results)
    
    return results
```

### DevOps & Monitoring

```python
from log_candy import *
import psutil
import requests

def system_health_check():
    log_info("🔍 Starting system health check...")
    
    # System resources
    system_stats = {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage('/').percent
    }
    log_debug(system_stats)
    
    # Health thresholds
    if system_stats["cpu_percent"] > 80:
        log_error(f"🚨 High CPU usage: {system_stats['cpu_percent']:.1f}%")
    elif system_stats["cpu_percent"] > 60:
        log_warning(f"⚠️ Elevated CPU usage: {system_stats['cpu_percent']:.1f}%")
    else:
        log_info(f"✅ CPU usage normal: {system_stats['cpu_percent']:.1f}%")
    
    # Service connectivity
    services = [
        {"name": "Database", "url": "http://db.internal:5432"},
        {"name": "Redis", "url": "http://cache.internal:6379"},
        {"name": "API Gateway", "url": "http://api.internal:8080/health"}
    ]
    
    for service in services:
        try:
            response = requests.get(service["url"], timeout=5)
            if response.status_code == 200:
                log_result(f"✅ {service['name']}: Healthy")
            else:
                log_warning(f"⚠️ {service['name']}: Status {response.status_code}")
        except Exception as e:
            log_error(f"💥 {service['name']}: Connection failed - {e}")
```

## 📖 Complete API Reference

### Core Logging Functions

| Function | Description | Example |
|----------|-------------|---------|
| `log_debug(message)` | Debug-level logging (purple) | `log_debug("Variable state: x=5")` |
| `log_info(message)` | Info-level logging (blue) | `log_info("Process started")` |
| `log_result(message)` | Result logging (green) | `log_result("Task completed")` |
| `log_warning(message)` | Warning logging (yellow) | `log_warning("Low memory")` |
| `log_error(message)` | Error logging (red) | `log_error("Connection failed")` |

### Configuration Functions

| Function | Parameters | Description |
|----------|------------|-------------|
| `set_log_level(level)` | `level: str` | Set minimum log level ('DEBUG', 'INFO', 'RESULT', 'WARNING', 'ERROR') |
| `get_log_level()` | None | Get current log level as string |
| `set_compact_formatting(enabled, threshold)` | `enabled: bool`, `threshold: int` | Configure object formatting |
| `get_formatting_settings()` | None | Get current formatting configuration |

### Special Functions

| Function | Parameters | Description |
|----------|------------|-------------|
| `tqdm_info(message)` | `message: Any` | Returns formatted info message for progress bars |
| `input_debug(message)` | `message: Any` | Interactive input with debug-style prompt |

### Constants

| Constant | Description |
|----------|-------------|
| `LOG_LEVELS` | Dictionary mapping level names to numeric values |

## 🔧 Requirements & Dependencies

- **Python**: 3.6 or higher
- **Dependencies**: 
  - `tqdm==4.66.4` (for progress bar integration)

## 🎮 Getting Started Examples

Want to see all features in action? Create a test file and try these examples:

```python
# test_log_candy.py
from log_candy import *

def demo_basic_features():
    """Try all the basic features of Log Candy"""
    
    # Test all log levels
    log_debug("🔧 Debug: Checking variable states")
    log_info("📊 Info: Process started")  
    log_result("✅ Result: Task completed successfully")
    log_warning("⚠️ Warning: Memory usage high")
    log_error("💥 Error: Connection failed")
    
    # Test different object types
    log_info("Simple string")
    log_debug({"user": "Alice", "score": 95, "active": True})
    log_result([1, 2, 3, "success", {"nested": "data"}])
    
    # Test log level control
    print("\n🎚️ Testing log level control:")
    set_log_level('WARNING')
    log_debug("This debug won't show")
    log_info("This info won't show") 
    log_warning("This warning will show")
    
    # Reset to show all
    set_log_level('DEBUG')
    log_info("Back to showing all levels!")

if __name__ == "__main__":
    demo_basic_features()
```

Run it with:
```bash
python test_log_candy.py
```

The examples cover:
- 🎯 All 5 log levels with real-world examples
- 📦 Different object types (strings, numbers, lists, dicts, custom objects)
- 🎚️ Log level filtering demonstration  
- 🎨 Object formatting examples

## 🤝 Contributing

We welcome contributions! Whether it's bug fixes, new features, documentation improvements, or examples, your help makes Log Candy better for everyone.

### 🚀 Ways to Contribute

- 🐛 **Bug Reports**: Found an issue? [Open an issue](https://github.com/SabeeenoGH/log-candy/issues)
- 💡 **Feature Requests**: Have an idea? We'd love to hear it!
- 📝 **Documentation**: Help improve our docs and examples
- 🔧 **Code**: Submit pull requests for bug fixes or new features
- 🧪 **Testing**: Help us test across different Python versions and environments

### 🎯 What We're Looking For

- 🌈 **New color themes or customization options**
- 📊 **Integration with popular logging frameworks**
- 🔧 **Performance improvements**
- 📱 **Better formatting for specific object types**
- 🧪 **More comprehensive tests**
- 📚 **Usage examples and tutorials**

## 🙏 Acknowledgements

- **Contributors**: Thank you to all contributors who help make Log Candy better!
- **Community**: Special thanks to everyone who uses Log Candy and provides feedback
- **Inspiration**: Built with love for the Python community and beautiful terminal output

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Show Your Support

If Log Candy helps make your debugging more delightful, consider:

- ⭐ **Starring the repository** on GitHub
- 🐦 **Sharing** with your developer friends
- 💝 **Contributing** to the project
- 📝 **Writing about your experience** with Log Candy

---

**Happy Logging! 🍭✨**

*Made with ❤️ by [Sabino Roccotelli](https://github.com/SabeeenoGH)*