# -*- coding: utf-8 -*-
#
import time
from datetime import datetime

def get_timestamp():
    return time.time()

def get_utc_datetime():
    """
    Get UTC datetime
    """
    dt = datetime.utcnow()
    return dt.isoformat(sep=' ')

# TODO: Add other get_xxx_datetime() for different timezone.
# def get_cst_datetime():
#    pass

# TODO: Add convert function for different timezone.
