# **RIFM - RESTful Interface For MongoDB**

## **Requirements**

- MongoDB
- Python 3.6
- Flask
- Flask-RESTful
- pymongo
- pytest
- pytest-flask

## **Http Response**

### **Response Message**

- Create/Update success! ID:\<MongoDB document id\>
- Create/Update failed!

### **Response Code**

- 200: OK
- 201: Created
- 204: No Contect
- 405: Method not allowed
- 417: Expectation Failed

## **MongoDB Design And Usage**

### **Signal Element (1st Level)**

**Collection Design:**

| Field(L1)        | Field(L2) | Description                                      |
| ---------------- | --------- | ------------------------------------------------ |
| _id              |           | <datatime+business_type+serial_number>           |
| satellite        |           | <satellite_id>                                   |
| antenna_id       |           | <antenna_id_value>                               |
| polarity         |           | <polarity_method>                                |
| frequency        |           | <frequency_value>                                |
| modulation_type  |           | <modulation_type_value>                          |
| modulation_rate  |           | <modulation_rate_value>                          |
| channel_coding   |           | <channel_coding>                                 |
| data_source_type |           | <data_source_type> (exp.: master/vsat station)   |
| demodulator_id   |           | <demodulator_id_value>                           |
| frame_type       |           | <frame_type_value> (exp.: control frame/ip data) |
| storage_path     |           | <file_storage_path>                              |
| time_stamp       |           | <time_stamp_value>                               |
| create           | user      | <input_user_name>                                |
|                  | time      | <create_date_time>                               |
| modify           | user      | <modify_user_name>                               |
|                  | time      | <modify_date_time>                               |

**Usage:**

- Create one document using 'POST'.

```(cmd)
curl -X POST \
    -H "Content-Type:application/json" \
    -d '{
        "_id":"<time+business_type+sn>",
        "satellite":"<satellite_id>",
        "antenna_id":"<antenna_id>",
        "polarity":"<polarity_method>",
        "frequency":"<frequency_value>",
        "modulation_type":"<modulation_type_value>",
        "modulation_rate":"<modulation_rate_value>",
        "channel_coding":"<channel_coding>",
        "data_source_type":"<data_source_type>",
        "demodulator_id":"<demodulator_id_value>",
        "frame_type":"<frame_type_value>",
        "storage_path":"<file_storage_path>",
        "time_stamp":"<time_stamp_value>",
        "create": {
            "user":"<create_user_name>"
        }
    }' \
    http://<FQDN>:27080/<db_name>/l1_signal_element
```

Note: RIFM will add create datetime automatically.

- Find one document by '_id'

```(cmd)
curl -X GET http://<FQDN>:27080/<db_name>/l1_signal_element/<string:_id>
```

- Update some fields in one document using 'PUT'

```(cmd)
curl -X PUT \
    -H "Content-Type:application/json" \
    -d '{
        "$set": {
            "satellite":"<update_satellite_id>",
            "channel_coding":"<update_channel_coding>",
            "frame_type":"<update_frame_type_value>",
            "storage_path":"<update_file_storage_path>",
            "modify.user":"<modify_user_name>"
        }
    }' \
    http://<FQDN>:27080/<db_name>/l1_signal_element/<string:_id>
```

Note: RIFM will add create datetime automatically.

or

```(cmd)
curl -X PUT \
    -H "Content-Type:application/json" \
    -d '{
        "$set": {
            "satellite":"<update_satellite_id>",
            "channel_coding":"<update_channel_coding>",
            "frame_type":"<update_frame_type_value>",
            "storage_path":"<update_file_storage_path>"
        }
    }' \
    http://<FQDN>:27080/<db_name>/l1_signal_element/<string:_id>
```

Note: You can update one or more fields at a time. But update modify user always.

- Delete one document by '_id' Using 'DELETE'

```(cmd)
<<<<<<< HEAD
curl -X DELETE http://<FQDN>:27080/dev/l1_signal_element/<string:_id>
=======
curl -X DELETE http://<FQDN>:27080/<db_name>/l1_signal_element/<string:_id>
>>>>>>> dev
```

### **Control Frame (2nd Level)**

**Collection Design:**

| Field(L1)    | Field(L2) | Description                                          |
| ------------ | --------- | ---------------------------------------------------- |
| _id          |           | <datatime+business_type+serial_number>               |
| src_id       |           | <source_data_id(l1_signal_element id)>               |
| type         |           | <frame_type> (exp.:0xDC,0xDD,0x40,6 bytes frame,...) |
| storage_path |           | <file_storage_path>                                  |
| time_stamp   |           | <time_stamp_value>                                   |
| create       | name      | <create_user_name>                                   |
|              | time      | <create_date_time>                                   |
| modify       | name      | <modify_date_time>                                   |
|              | time      | <modify_date_time>                                   |

**Usage:**

- Create one document using 'POST'.

```(cmd)
curl -X POST \
    -H "Content-Type:application/json" \
    -d '{
        "_id":"<time+business_type+sn>",
        "src_id":"<source_id_data(Level1)>",
        "type":"<frame_type>",
        "storage_path":"<file_storage_path>",
        "time_stamp":"<time_stamp_value>",
        "create": {
            "user":"<create_user_name>"
        }
    }' \
    http://<FQDN>:27080/<db_name>/l2_control_frame
```

Note: RIFM will add create datetime automatically.

- Find one document by '_id'

```(cmd)
curl -X GET http://<FQDN>:27080/<db_name>/l2_control_frame/<string:_id>
```

- Update some fields in one document using 'PUT'

```(cmd)
curl -X PUT \
    -H "Content-Type:application/json" \
    -d '{
        "$set": {
            "type":"<update_frame_type>",
            "storage_path":"<update_file_storage_path>",
            "modify.user":"<modify_user_name>"
        }
    }' \
    http://<FQDN>:27080/<db_name>/l2_control_frame/<string:_id>
```

Note: RIFM will add create datetime automatically.

or

```(cmd)
curl -X PUT \
    -H "Content-Type:application/json" \
    -d '{
        "$set": {
            "type":"<update_frame_type>",
            "storage_path":"<update_file_storage_path>"
        }
    }' \
    http://<FQDN>:27080/<db_name>/l2_control_frame/<string:_id>
```

Note: You can update one or more fields at a time. But update modify user always.

- Delete one document by '_id' Using 'DELETE'

```(cmd)
<<<<<<< HEAD
curl -X DELETE http://<FQDN>:27080/dev/l2_control_frame/<string:_id>
=======
curl -X DELETE http://<FQDN>:27080/<db_name>/l2_control_frame/<string:_id>
>>>>>>> dev
```

### **IP Data (2nd Level)**

**Collection Design:**

| Field(L1)    | Field(L2) | Description                            |
| ------------ | --------- | -------------------------------------- |
| _id          |           | <datatime+business_type+serial_number> |
| src_id       |           | <source_data_id(l1_signal_element id)> |
| encrypted    |           | <y/n>                                  |
| 1st_layer_ip | protocol  | <network_protocol>                     |
|              | src_ip    | <src_ip>                               |
|              | dst_ip    | <dst_ip>                               |
|              | src_port  | <src_port>                             |
|              | dst_port  | <dst_port>                             |
| 2nd_layer_ip | protocol  | <network_protocol>                     |
|              | src_ip    | <src_ip>                               |
|              | dst_ip    | <dst_ip>                               |
|              | src_port  | <src_port>                             |
|              | dst_port  | <dst_port>                             |
| 3rd_layer_ip | protocol  | <network_protocol>                     |
|              | src_ip    | <src_ip>                               |
|              | dst_ip    | <dst_ip>                               |
|              | src_port  | <src_port>                             |
|              | dst_port  | <dst_port>                             |
| storage_path |           | <file_storage_path>                    |
| time_stamp   |           | <time_stamp_value>                     |
| create       | user      | <create_user_name>                     |
|              | time      | <create_date_time>                     |
| modify       | user      | <modify_user_name>                     |
|              | time      | <modify_date_time>                     |

**Usage:**

- Create one document using 'POST'.

```(cmd)
curl -X POST \
    -H "Content-Type:application/json" \
    -d '{
        "_id":"<time+business_type+sn>",
        "src_id":"<source_id_data(Level1)>",
        "encrypted":"<y/n>",
        "1st_layer_ip": {
            "protocol":"<network_protocol>",
            "src_ip":"<src_ip>",
            "dst_ip":"<dst_ip>",
            "src_port":"<src_port>",
            "dst_port":"<dst_port>"
        },
        "2nd_layer_ip": {
            "protocol":"<network_protocol>",
            "src_ip":"<src_ip>",
            "dst_ip":"<dst_ip>",
            "src_port":"<src_port>",
            "dst_port":"<dst_port>"
        },
        "3rd_layer_ip": {
            "protocol":"<network_protocol>",
            "src_ip":"<src_ip>",
            "dst_ip":"<dst_ip>",
            "src_port":"<src_port>",
            "dst_port":"<dst_port>"
        },
        "storage_path":"<file_storage_path>",
        "time_stamp":"<time_stamp_value">,
        "create": {
            "user":"<create_user_name>"
        }
    }' \
    http://<FQDN>:27080/<db_name>/l2_ip_data
```

Note: RIFM will add create datetime automatically.

- Find one document by '_id'

```(cmd)
curl -X GET http://<FQDN>:27080/<db_name>/l2_ip_data/<string:_id>
```

- Update some fields in one document using 'PUT'

```(cmd)
curl -X PUT \
    -H "Content-Type:application/json" \
    -d '{
        "$set": {
            "1st_layer_ip.protocol":"<network_protocol>",
            "1st_layer_ip.src_ip":"<update_ip_address>",
            "1st_layer_ip.dst_ip":"<update_ip_address>",
            "storage_path":"<update_file_storage_path>",
            "modify.user":"<modify_user_name>"
        }
    }' \
    http://<FQDN>:27080/<db_name>/l2_ip_data/<string:_id>
```

Note: RIFM will add create datetime automatically.

or

```(cmd)
curl -X PUT \
    -H "Content-Type:application/json" \
    -d '{
        "$set": {
            "3rd_layer_ip.protocol":"<network_protocol>",
            "3rd_layer_ip.src_ip":"<update_ip_address>",
            "3rd_layer_ip.dst_ip":"<update_ip_address>",
            "storage_path":"<update_file_storage_path>",
        }
    }' \
    http://<FQDN>:27080/<db_name>/l2_ip_data/<string:_id>
```

Note: You can update one or more fields at a time. But update modify user always.

- Delete one document by '_id' Using 'DELETE'

```(cmd)
<<<<<<< HEAD
curl -X DELETE http://<FQDN>:27080/dev/l2_ip_data/<string:_id>
=======
curl -X DELETE http://<FQDN>:27080/<db_name>/l2_ip_data/<string:_id>
>>>>>>> dev
```

### **E-mail (3rd Level)**

**Collection Design:**

| Field(L1)       | Field(L2) | Description                            |
| --------------- | --------- | -------------------------------------- |
| _id             |           | <datatime+business_type+serial_number> |
| src_id          |           | <source_data_id(l2_ip_data id)>        |
| title           |           | <email_title>                          |
| from            |           | <from_address>                         |
| to              |           | <to_address>                           |
| attachment_tpye |           | <attachment_type> (exp.:pdf)           |
| storage_path    |           | <file_storage_path>                    |
| time_stamp      |           | <time_stamp_value>                     |
| create          | user      | <create_user_name>                     |
|                 | time      | <create_date_time>                     |
| modify          | user      | <modify_user_name>                     |
|                 | time      | <modify_date_time>                     |

**Usage:**

- Create one document using 'POST'

```(cmd)
curl -X POST \
    -H "Content-Type:application/json" \
    -d '{
        "_id":"<time+business_type+sn>",
        "src_id":"<source_id_data(Level2)>",
        "from":"<from_addresss>",
        "to":"<to_address>",
        "title":"<email_title>",
        "storage_path":"<file_storage_path>",
        "time_stamp":"<time_stamp_value>",
        "create": {
            "user":"<create_user_name>"
        }
    }' \
    http://<FQDN>:27080/<db_name>/l3_email
```

Note: RIFM will add create datetime automatically.

- Find one document by '_id'

```(cmd)
curl -X GET http://<FQDN>:27080/<db_name>/l3_email/<string:_id>
```

- Update some fields in one document using 'PUT'

```(cmd)
curl -X PUT \
    -H "Content-Type:application/json" \
    -d '{
        "$set": {
            "title":"<update_email_title>",
            "from":"<update_from_address>",
            "to":"<update_to_address>",
            "storage_path":"<update_file_storage_path>",
            "modify.user":"<modify_user_name>"
        }
    }' \
    http://<FQDN>:27080/<db_name>/l3_email/<string:_id>
```

Note: RIFM will add create/modify datetime automatically.

or

```(cmd)
curl -X PUT \
    -H "Content-Type:application/json" \
    -d '{
        "$set": {
            "title":"<update_email_title>",
            "from":"<update_email_from_address>",
            "to":"<update_email_to_address>",
            "stroage_path":"<update_file_storage_path>",
        }
    }' \
    http://<FQDN>:27080/<db_name>/l3_email/<string:_id>
```

Note: You can update one or more fields at a time. But update modify user always.

- Delete one document by '_id' Using 'DELETE'

```(cmd)
<<<<<<< HEAD
curl -X DELETE http://<FQDN>:27080/dev/l3_email/<string:_id>
=======
curl -X DELETE http://<FQDN>:27080/<db_name>/l3_email/<string:_id>
>>>>>>> dev
```

### **HTTP (3rd Level)**

**Collection Design:**

| Field (L1)   | Field (L2) | Description                        |
| ------------ | ---------- | ---------------------------------- |
| _id          |            | <time+business_type+serial_number> |
| src_id       |            | <source_data_id(l2_ip_data id)>    |
| title        |            | <http_page_title>                  |
| type         |            | <http_file_type>                   |
| storage_path |            | <file_storage_path>                |
| time_stamp   |            | <time_stamp_value>                 |
| create       | user       | <create_user_name>                 |
|              | time       | <create_date_time>                 |
| modify       | user       | <last_modify_user>                 |
|              | time       | <last_modify_time>                 |

**Usage:**

- Create one document using 'POST'.

```(cmd)
curl -X POST \
    -H "Content-Type:application/json" \
    -d '{
        "_id":"<time+business_type+serial_number>",
        "src_id":"<source_id_data(Level2)>",
        "title":"<http_page_title>",
        "type":"<http_file_type>",
        "storage_path":"<file_storage_path>",
        "time_stamp":"<time_stamp_value>",
        "create": {
            "user":"<create_user_name>"
        }
    }' \
    http://<FQDN>:27080/<db_name>/l3_http
```

Note: RIFM will add create datetime automatically.

- Find one document by '_id'

```(cmd)
curl -X GET http://<FQDN>:27080/<db_name>/l3_http/<string:_id>
```

- Update some fields in one document using 'PUT'

```(cmd)
curl -X PUT \
    -H "Content-Type:application/json" \
    -d '{
        "$set": {
            "storage_path":"<update_file_storage_path>",
            "modify.user":"<modify_user_name>"
        }
    }' \
    http://<FQDN>:27080/<db_name>/l3_http/<string:_id>
```

or

```(cmd)
curl -X PUT \
    -H "Content-Type:application/json" \
    -d '{
        "$set": {
            "title":"<update_http_page_title>",
            "type":"<update_http_file_type>",
            "storage_path":"<update_file_storage_path>",
            "create.user":"<update_user_name>",
            "modify.user":"<modify_user_name>"
        }
    }' \
    http://<FQDN>:27080/<db_name>/l3_http/<string:_id>
```

Note: You can update one or more fields at a time. But update modify user always.

- Delete one document by '_id' Using 'DELETE'

```(cmd)
<<<<<<< HEAD
curl -X DELETE http://<FQDN>:27080/dev/l3_http/<string:_id>
=======
curl -X DELETE http://<FQDN>:27080/<db_name>/l3_http/<string:_id>
>>>>>>> dev
```

## TODO

- GET function
- Think about Import Flask-Pymongo
- Think about mongodb 'close()' or use one instance connection.