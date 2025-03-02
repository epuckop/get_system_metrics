# get_system_metrics

## Overview
A Python utility for retrieving and monitoring system metrics.

## Features
- Collect system performance metrics
- Easy-to-use interface

## Installation
```bash
pip install get_system_metrics
```

## Usage
```python
from get_system_metrics import SystemMetrics

# Get current system metrics
metrics = SystemMetrics()
print(metrics.cpu_usage())
print(metrics.memory_usage())
print(metrics.disk_usage())
```

## Requirements
- Python 3.7+
- psutil library

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
MIT License - See the [LICENSE](LICENSE) file for details

## Author
Dmitry Goldenberg