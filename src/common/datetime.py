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

def check_create(
    data: dict(type=dict, help='JSON string to be checked'),
):
    """
    Check recored 'create' information.
    """
    # check 'create' field
    if 'create' not in data:
        data.setdefault('create', {})
    # check 'create.user' field
    if 'user' not in data['create']:
        data['create']['user'] = 'anonymous'
    # add field 'create.time'
    data['create']['time'] = get_utc_datetime()
    # return new json data string
    return data

def check_modify(
    data: dict(type=dict, help='JSON string to be modify')
):
    """
    Check record 'modify' information.
    """
    # check 'modify' field
    if 'modify.user' not in data['$set']:
        data['$set'].setdefault('modify.user', 'anonymous')
    # add field 'modify.time'
    data['$set'].setdefault('modify.time', get_utc_datetime())
    # return new json data string
    return data