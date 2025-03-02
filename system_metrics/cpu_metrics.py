import psutil

def get_cpu_usage(interval=1):
    """
    Get CPU usage metrics.
    
    Args:
        interval (float): Time interval for measuring CPU usage
    
    Returns:
        dict: CPU usage metrics
    """
    # Overall CPU usage
    cpu_percent = psutil.cpu_percent(interval=interval)
    
    # Per-core CPU usage
    per_core_usage = psutil.cpu_percent(interval=interval, percpu=True)
    
    return {
        'total_usage': cpu_percent,
        'per_core_usage': per_core_usage
    }