import time
from datetime import datetime


def current_milli_time():
    """
    Returns the current time, rounded to the nearest millionth of a second.
    """
    return int(round(time.time() * 1000))


def get_timestamp():
    return datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H-%M-%S')
