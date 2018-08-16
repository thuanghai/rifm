# README

## Abstract

Test file (*.py) in this directory which I has writed for pytest.
Test methods are taked into a class. You can check it in pytest document "Group multiple tests in a class".

<https://docs.pytest.org/en/latest/getting-started.html>

And the pytest pulgin 'pytest-flask' is also used here.
Every method has argument - 'client'.

## Instruction for pytest-flask

Although pytest-flask has an application test client for class-based tests like below:

```(python)
@pytest.mark.usefixtures('client_class')
class TestSuite:

    def test_myview(self):
        assert self.client.get(url_for('myview')).status_code == 200
```

pylint will give message:
> E1101:Instance of 'TestSuite' has no 'client' member.

Here is my attempt:

```(python)
#
# Using 'client_class' fixtures for class-based tests below is another method.
# but pylint will give error message that looks bad although the test code run successfully.
#
# Group multiple tests in a class
# client_class - application test client for class-based tests
#
@pytest.mark.usefixtures('client_class')
class TestL1SignalElement():
    # document '_id' in mongodb during the test
    __test_id = 'test_l1_signal_element_type-' + str(get_timestamp())

    def test_post(self):
        """
        Test client post method for insert one document
        """
        # set insert document '_id'
        # insert_id = self.__get_test_id()
        insert_id = self.__test_id
        print(insert_id)
        # set insert document data
        test_insert_data = {
            '_id':insert_id,
            'satellite':'test_satellite_name',
            'antenna_id':'test_antenna_id_value',
            'polarity':'test_polarity_method',
            'frequency':'test_frequency_value',
            'modulation_type':'test_modulation_type_value',
            'modulation_rate':'test_modulation_rate_value',
            'channel_coding':'test_channel_coding',
            'data_source_type':'master/vsat station',
            'demodulator_id':'demodulator_id_value',
            'frame_type':'control-frame or ip-data',
            'storage_path': '/vol/data/signal_element/test_signal-element_file',
            'time_stamp':'input_your_time_stamp',
            'create': {
                'user':'test'
            }
        }

        chkresponse = self.client.post(
            url_for('api.l1_signal_element'),
            json = test_insert_data
        )
        # Note1:
        # Ignore pylint error message below and And the pytest can running normally.
        # > E1101:Instance of 'TestL1SignalElement' has no 'client' member.
        # 
        # Note2:
        # Passing the json argument in the test_client method
        # 1. It sets the request data to the JSON-serialized object
        # 2. It sets the content type to application/json.
        # 3. You can get the JSON data from request or response with get_json.
        assert chkresponse.status_code == 201
```

## How to use 'url_for'

How to build url using 'url_for', you can see 'Flask Quick Start' or this code below:

```(python)
from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'
@app.route('/login')
def login():
    return 'login'
@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

/
/login
/login?next=/
/user/John%20Doe
```