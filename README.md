# **RIFM - RESTful Interface For MongoDB**

## **Requirements**

- MongoDB
- Python 3.6
- Flask
- Flask-RESTful
- pymongo

## **Http Code**

- 200: OK
- 201: Created
- 204: No Contect
- 417: Expectation Failed

## **MongoDB Design And Usage**

### **Signal Element (1st Level)**

| DB Field Name    | Description                                      |
| ---------------- | ------------------------------------------------ |
| _id              | <datatime+business_type+serial_number>           |
| satellite        | <satellite_id>                                   |
| antenna_id       | <antenna_id_value>                               |
| polarity         | <polarity_method>                                |
| frequency        | <frequency_value>                                |
| modulation_type  | <modulation_type_value>                          |
| modulation_rate  | <modulation_rate_value>                          |
| channel_coding   | <channel_coding>                                 |
| data_source_type | <data_source_type> (exp.: master/vsat station)   |
| demodulator_id   | <demodulator_id_value>                           |
| time_stamp       | <time_stamp_value>                               |
| frame_type       | <frame_type_value> (exp.: control frame/ip data) |
| file_path        | <file_storage_path>                              |
| input_user       | <input_user_name>                                |
| input_time       | <input_date_time>                                |

**Usage:**

```(cmd)
curl -X POST \
    -H "Content-Type:application/json" \
    -d '{
        "number":"<time+business_type+sn>",
        "satellite":"<satellite_id>",
        "antenna_id":"<antenna_id>",
        "polarity":"<polarity_method>",
        "frequency":"<frequency_value>",
        "modulation_type":"<modulation_type_value>",
        "modulation_rate":"<modulation_rate_value>",
        "channel_coding":"<channel_coding>",
        "data_source_type":"<data_source_type>",
        "demodulator_id":"<demodulator_id_value>",
        "time_stamp":"<time_stamp_value>",
        "frame_type":"<frame_type_value>",
        "file_path":"<file_storage_path>",
        "input_user":"<input_user_name>",
        "input_time":"<input_date_time>"
    }' \
    http://<FQDN>:27080/dev/l1_signal_element
```

### **Control Frame (2nd Level)**

| DB Field Name | Description                                          |
| ------------- | ---------------------------------------------------- |
| _id           | <datatime+business_type+serial_number>               |
| type          | <frame_type> (exp.:0xDC,0xDD,0x40,6 bytes frame,...) |
| file_path     | <file_storage_path>                                  |
| input_user    | <input_user_name>                                    |
| input_time    | <input_date_time>                                    |

**Usage:**

```(cmd)
curl -X POST \
    -H "Content-Type:application/json" \
    -d '{
        "number":"<time+business_type+sn>",
        "type":"<frame_type>",
        "file_path":"<file_storage_path>",
        "input_user":"<input_user_name>",
        "input_time":"<input_date_time>",
    }' \
    http://<FQDN>:27080/dev/l2_control_frame
```

### **IP Data (2nd Level)**

| DB Field Name |          | Description                            |
| ------------- | -------- | -------------------------------------- |
| _id           |          | <datatime+business_type+serial_number> |
| encrypted     |          | <y/n>                                  |
| 1st_layer_ip  | protocol | <network_protocol>                     |
|               | src_ip   | <src_ip>                               |
|               | dst_ip   | <dst_ip>                               |
|               | src_port | <src_port>                             |
|               | dst_port | <dst_port>                             |
| 2nd_layer_ip  | protocol | <network_protocol>                     |
|               | src_ip   | <src_ip>                               |
|               | dst_ip   | <dst_ip>                               |
|               | src_port | <src_port>                             |
|               | dst_port | <dst_port>                             |
| 3rd_layer_ip  | protocol | <network_protocol>                     |
|               | src_ip   | <src_ip>                               |
|               | dst_ip   | <dst_ip>                               |
|               | src_port | <src_port>                             |
|               | dst_port | <dst_port>                             |
| file_path     |          | <file_storage_path>                    |
| input_user    |          | <input_user_name>                      |
| input_time    |          | <input_date_time>                      |

**Usage:**

```(cmd)
curl -X POST \
    -H "Content-Type:application/json" \
    -d '{
        "number":"<time+business_type+sn>",
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
        "file_path":"<file_storage_path>"
        "input_user":"<input_user_name>",
        "input_time":"<input_date_time>"
    }' \
    http://<FQDN>:27080/dev/l2_ip_data
```

### **E-mail (3rd Level)**

| Field(L1)       | Field(L2) | Description                            |
| --------------- | --------- | -------------------------------------- |
| _id             |           | <datatime+business_type+serial_number> |
| title           |           | <email_title>                          |
| from            |           | <from_address>                         |
| to              |           | <to_address>                           |
| attachment_tpye |           | <attachment_type> (exp.:pdf)           |
| storage_path    |           | <file_storage_path>                    |
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
        "number":"<time+business_type+sn>",
        "from":"<from_addresss>",
        "to":"<to_address>",
        "title":"<email_title>",
        "storage_path":"<file_storage_path>",
        "create": {
            "user":"<create_user_name>",
            "time":"<create_date_time>"
        }
    }' \
    http://<FQDN>:27080/dev/l3_email
```

- Update one document using 'PUT'

```(cmd)
curl -X PUT \
    -H "Content-Type:application/json" \
    -d '{
        "$set": {
            "storage_path":"<update_file_storage_path>",
            "modify.user":"<modify_user_name>"
        }
    }' \
    http://<FQDN>:27080/dev/l3_email/<string:_id>
```

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
            "create.user":"<update_user_name>",
            "modify.user":"<modify_user_name>"
        }
    }' \
    http://<FQDN>:27080/dev/l3_email/<string:_id>
```

Note: You can update one or more fields at a time. But update modify user always.

### **HTTP (3rd Level)**

| Field (L1)   | Field (L2) | Description                        |
| ------------ | ---------- | ---------------------------------- |
| _id          |            | <time+business_type+serial_number> |
| src_id       |            | <ip_data_id>                       |
| title        |            | <http_page_title>                  |
| type         |            | <http_file_type>                   |
| storage_path |            | <file_storage_path>                |
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
        "title":"<http_page_title>",
        "type":"<http_file_type>",
        "storage_path":"<file_storage_path>",
        "create": {
            "user":"<create_user_name>",
            "time":"<create_date_time>"
        }
    }' \
    http://<FQDN>:27080/dev/l3_http
```

- Update one document using 'PUT'

```(cmd)
curl -X PUT \
    -H "Content-Type:application/json" \
    -d '{
        "$set": {
            "storage_path":"<update_file_storage_path>",
            "modify.user":"<modify_user_name>"
        }
    }' \
    http://<FQDN>:27080/dev/l3_http/<string:_id>
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
    http://<FQDN>:27080/dev/l3_http/<string:_id>
```

Note: You can update one or more fields at a time. But update modify user always.