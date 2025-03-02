import shutil

def get_disk_usage(path='/'):
    """
    Get disk usage metrics for a specified path.
    
    Args:
        path (str): Path to check disk usage. Defaults to root directory.
    
    Returns:
        dict: Disk usage metrics in percentages and bytes
    """
    # Get disk usage
    disk = shutil.disk_usage(path)
    
    return {
        'total': disk.total,
        'used': disk.used,
        'free': disk.free,
        'percent': disk.used / disk.total * 100
    }