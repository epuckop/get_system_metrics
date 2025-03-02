import psutil

def get_ram_usage():
    """
    Get RAM usage metrics.
    
    Returns:
        dict: RAM usage metrics in percentages and bytes
    """
    # Get memory information
    memory = psutil.virtual_memory()
    
    return {
        'total': memory.total,
        'available': memory.available,
        'used': memory.used,
        'percent': memory.percent,
        'free': memory.free
    }