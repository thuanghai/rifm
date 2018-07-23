# -*- coding: utf-8 -*-
import datetime
import random
import pytest
import json

from flask import url_for
from src.resources.l1_signal_element import SignalElement

def test_get(client):
    """
    Test client get method for null
    """
    chkresponse = client.get(url_for('api.l1_signal_element'))
    assert chkresponse.status_code == 200

def test_post(client):
    """
    Test client post method for insert one document
    """
    # | DB Field Name    | Description                                      |
    # | ---------------- | ------------------------------------------------ |
    # | number           | <datatime+business_type+serial_number>           |
    # | satellite        | <satellite_id>                                   |
    # | antenna_id       | <antenna_id_value>                               |
    # | polarity         | <polarity_method>                                |
    # | frequency        | <frequency_value>                                |
    # | modulation_type  | <modulation_type_value>                          |
    # | modulation_rate  | <modulation_rate_value>                          |
    # | channel_coding   | <channel_coding>                                 |
    # | data_source_type | <data_source_type> (exp.: master/vsat station)   |
    # | demodulator_id   | <demodulator_id_value>                           |
    # | time_stamp       | <time_stamp_value>                               |
    # | frame_type       | <frame_type_value> (exp.: control frame/ip data) |
    # | file_path        | <file_storage_path>                              |
    # | input_user       | <input_user_name>                                |
    # | input_time       | <input_date_time>                                |
    # get current time
    nowTime = str(datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S'))
    test_number = nowTime + '_type_' + str(random.randint(1, 9999999))
    test_post_data = {
        'number':test_number,
        'satellite':'test_satellite_name',
        'antenna_id':'test_antenna_id_value',
        'polarity':'test_polarity_method',
        'frequency':'test_frequency_value',
        'modulation_type':'test_modulation_type_value',
        'modulation_rate':'test_modulation_rate_value',
        'channel_coding':'test_channel_coding',
        'data_source_type':'master/vsat station',
        'demodulator_id':'demodulator_id_value',
        'time_stamp':'time_stamp_value',
        'frame_type':'control-frame / ip-data',
        'file_path':'test_file_path',
        'input_user':'test_kowalski',
        "input_time": nowTime
    }
    chkresponse = client.post(
        url_for('api.l1_signal_element'), 
        json = test_post_data
    )
    # Note:
    # Passing the json argument in the test_client method
    # 1. It sets the request data to the JSON-serialized object
    # 2. It sets the content type to application/json.
    # 3. You can get the JSON data from request or response with get_json.
    assert chkresponse.status_code == 201