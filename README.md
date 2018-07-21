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
| number           | <datatime+business_type+serial_number>           |
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
| number        | <datatime+business_type+serial_number>               |
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
| number        |          | <datatime+business_type+serial_number> |
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

| DB Field Name   | Description                            |
| --------------- | -------------------------------------- |
| number          | <datatime+business_type+serial_number> |
| title           | <email_title>                          |
| from            | <from_address>                         |
| to              | <to_address>                           |
| attachment_tpye | <attachment_type> (exp.:pdf)           |
| file_path       | <file_storage_path>                    |
| input_user      | <input_user_name>                      |
| input_time      | <input_date_time>                      |

**Usage:**

```(cmd)
curl -X POST \
    -H "Content-Type:application/json" \
    -d '{
        "number":"<time+business_type+sn>",
        "from":"<from_addresss>",
        "to":"<to_address>",
        "title":"email_title",
        "file_path":"<file_storage_path>",
        "input_user":"<input_user_name>",
        "input_time":"<input_date_time>"
    }' \
    http://<FQDN>:27080/dev/l3_email
```

### **HTTP (3rd Level)**

| DB Field Name | Description                            |
| ------------- | -------------------------------------- |
| number        | <datatime+business_type+serial_number> |
| type          | <file_type>                            |
| title         | <page_title>                           |
| file_path     | <file_storage_path>                    |
| input_user    | <input_user_name>                      |
| input_time    | <input_date_time>                      |

**Usage:**

```(cmd)
curl -X POST \
    -H "Content-Type:application/json" \
    -d '{
        "number":"<time+business_type+sn>",
        "type":"<file_type>",
        "title":"<page_title>",
        "file_path":"<file_storage_path>"
        "input_user":"<input_user_name>",
        "input_time":"<input_date_time>"
    }' \
    http://<FQDN>:27080/dev/l3_http
```
