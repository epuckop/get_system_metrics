import os
import json
import time
import pytz
from datetime import datetime
import logging

class MetricsLogger:
    def __init__(self, log_dir='./logs', 
                 log_levels=['normal', 'warning', 'critical'],
                 timezone=None,
                 log_format='json'):
        """
        Enhanced MetricsLogger with improved logging practices.
        
        Args:
            log_dir (str): Directory to save log files
            log_levels (list): Levels of logging to include
            timezone (str, optional): Timezone to use for local time
            log_format (str): Logging format ('json', 'structured', etc.)
        """
        self.log_dir = log_dir
        self.log_levels = log_levels
        self.log_format = log_format
        
        # Set timezone
        self.timezone = timezone or str(datetime.now().astimezone().tzinfo)
        try:
            self.tz_obj = pytz.timezone(self.timezone)
        except pytz.exceptions.UnknownTimeZoneError:
            self.tz_obj = datetime.now().astimezone().tzinfo
        
        # Ensure log directory exists
        os.makedirs(log_dir, exist_ok=True)
    
    def _determine_log_level(self, usage_percent):
        """
        Determine log level based on usage percentage.
        
        Args:
            usage_percent (float): Usage percentage
        
        Returns:
            str: Log level ('normal', 'warning', or 'critical')
        """
        usage_percent = round(usage_percent, 2)
        
        if usage_percent < 80:
            return 'normal'
        elif 80 <= usage_percent < 90:
            return 'warning'
        else:
            return 'critical'
    
    def log_metric(self, metric_name, usage_percent, additional_data=None):
        """
        Log a metric with enhanced logging practices.
        
        Args:
            metric_name (str): Name of the metric
            usage_percent (float): Usage percentage
            additional_data (dict, optional): Additional metric details
        """
        # Round usage_percent to 2 decimal places
        usage_percent = round(usage_percent, 2)
        
        # Determine log level
        log_level = self._determine_log_level(usage_percent)
        
        # Check if this log level is enabled
        if log_level not in self.log_levels:
            return
        
        # Prepare comprehensive log entry
        log_entry = {
            # Standardized Metadata
            'event': {
                'type': 'system_metric',
                'source': metric_name,
                'timestamp': {
                    'unix': int(time.time()),
                    'iso': datetime.now(pytz.utc).isoformat(),
                    'local': datetime.now(self.tz_obj).strftime('%Y-%m-%d %H:%M:%S')
                },
                'timezone': str(self.tz_obj)
            },
            
            # Metric-Specific Data
            'metric': {
                'name': metric_name,
                'usage_percent': usage_percent,
                'log_level': log_level
            },
            
            # Extended Context
            'context': additional_data or {}
        }
        
        # Create metric-specific log file
        log_file_path = os.path.join(self.log_dir, f'{metric_name}_metrics.log')
        
        # Append log entry to file
        with open(log_file_path, 'a') as log_file:
            json.dump(log_entry, log_file)
            log_file.write('\n')  # New line for readability