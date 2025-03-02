from .cpu_metrics import get_cpu_usage
from .ram_metrics import get_ram_usage
from .disk_metrics import get_disk_usage
from .metrics_logger import MetricsLogger

def system_monitoring(logger=None, log_levels=None):
    """
    Collect overall system resource usage and optionally log metrics.
    
    Args:
        logger (MetricsLogger, optional): Custom logger instance
        log_levels (list, optional): Log levels to include
    
    Returns:
        dict: Comprehensive system resource usage metrics
    """
    # Collect metrics
    cpu_metrics = get_cpu_usage()
    ram_metrics = get_ram_usage()
    disk_metrics = get_disk_usage()
    
    # Round percentages to 2 decimal places
    cpu_metrics['total_usage'] = round(cpu_metrics['total_usage'], 2)
    ram_metrics['percent'] = round(ram_metrics['percent'], 2)
    disk_metrics['percent'] = round(disk_metrics['percent'], 2)
    
    # Create logger if not provided
    if logger is None:
        logger = MetricsLogger(log_levels=log_levels or ['warning', 'critical'])
    
    # Log metrics ONLY ONCE
    logger.log_metric('cpu', cpu_metrics['total_usage'], 
                      {'per_core_usage': cpu_metrics['per_core_usage']})
    logger.log_metric('ram', ram_metrics['percent'], 
                      {'total': ram_metrics['total'], 'used': ram_metrics['used']})
    logger.log_metric('disk', disk_metrics['percent'], 
                      {'total': disk_metrics['total'], 'used': disk_metrics['used']})
    
    return {
        'cpu': cpu_metrics,
        'ram': ram_metrics,
        'disk': disk_metrics
    }