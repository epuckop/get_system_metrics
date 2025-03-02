import yaml
from system_metrics import system_monitoring
from system_metrics.metrics_logger import MetricsLogger

def load_config(config_path='./config.yaml'):
    """
    Load configuration from YAML file.
    
    Args:
        config_path (str): Path to the configuration file
    
    Returns:
        dict: Parsed configuration
    """
    try:
        with open(config_path, 'r') as config_file:
            return yaml.safe_load(config_file)
    except FileNotFoundError:
        print(f"Config file not found at {config_path}. Using default settings.")
        return {
            'metrics_logger': {
                'log_dir': './logs',
                'log_levels': ['warning', 'critical']
            }
        }
    except yaml.YAMLError as e:
        print(f"Error parsing config file: {e}")
        return {
            'metrics_logger': {
                'log_dir': './logs',
                'log_levels': ['warning', 'critical']
            }
        }

def main():
    # Load configuration
    config = load_config()
    
    # Extract logger configuration
    logger_config = config.get('metrics_logger', {})
    
    # Create logger with config
    logger = MetricsLogger(
        log_dir=logger_config.get('log_dir', './logs'),
        log_levels=logger_config.get('log_levels', ['warning', 'critical']),
        timezone=logger_config.get('timezone'),
        log_format=logger_config.get('log_format', 'json')
    )
    
    # Monitor system and log metrics
    system_metrics = system_monitoring(logger=logger)
    
    # Print usage details
    print(f"CPU Usage: {system_metrics['cpu']['total_usage']:.2f}%")
    print(f"RAM Usage: {system_metrics['ram']['percent']:.2f}%")
    print(f"Disk Usage: {system_metrics['disk']['percent']:.2f}%")

if __name__ == "__main__":
    main()