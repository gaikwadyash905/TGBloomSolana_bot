from datetime import datetime
from pytz import timezone

def get_us_time():
    """
    Retrieves the current time in the US Eastern Time Zone.

    This function leverages the `pytz` library to accurately 
    determine the current time in the US Eastern Time Zone, 
    accounting for Daylight Saving Time transitions. The time 
    is returned in the format `HH:MM:SS.mmm` (hours, minutes, 
    seconds, milliseconds).

    Returns:
        str: The current time as a string in the format `HH:MM:SS.mmm`.

    Example:
        >>> get_us_time()
        '14:32:45.123'
    
    Notes:
        - Ensure that the `pytz` library is installed in your environment 
          before using this function. You can install it using:
          `pip install pytz`.
        - The returned time string excludes microseconds beyond the 
          millisecond precision.
    """
    # Define the US Eastern timezone
    eastern = timezone("US/Eastern")
    
    # Get the current time in the specified timezone
    now = datetime.now(eastern)
    
    # Format the time to include hours, minutes, seconds, and milliseconds
    return now.strftime("%H:%M:%S.%f")[:-3]  # Format: HH:MM:SS.mmm
