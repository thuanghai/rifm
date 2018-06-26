**RIFM - RESTful Interface For MongoDB**
===

**Requirements**
---

- Mongodb
- Python 3.6
- Flask
- pymongo

**Http Code**
200:OK
201:Created
204:No Contect
417:Expectation Failed

**Usage**
---

Querying:

```(cmd)
curl -X GET \
    <host>//<class_name>
```

or

```(cmd)
curl -X GET "http://127.0.0.1:8000/person?where={'sex': 'male'}"
```

**Client example:**

```(cmd)
curl -X POST \
    -H "Content-Type: application/json" \
    -d '{"name": "Alice", \
        "sex": "male", \
        "birth": "1983-01-01"}'\
     http://127.0.0.1/person
```

```(cmd)
curl -X POST -H "Content-Type: application/json" -d '{"name": "Alice", "sex": "female", "birth": "1983-01-01", "age": 10}' http://127.0.0.1:8000/person
curl -X POST -H "Content-Type: application/json" -d '{"name": "Alice2", "sex": "female", "birth": "1983-02-01", "age": 20}' http://127.0.0.1:8000/person
curl -X POST -H "Content-Type: application/json" -d '{"name": "Bob", "sex": "male", "birth": "1983-01-01", "age": 10}' http://127.0.0.1:8000/person
curl -X POST -H "Content-Type: application/json" -d '{"name": "Bob2", "sex": "male", "birth": "1983-02-01", "age": 20}' http://127.0.0.1:8000/person
```

**Query document:**

```(cmd)
curl -X GET http://localhost:8000/demo/person/5b022c91d42b3421843b5246
```

**Update document:**

```(cmd)
curl -X PUT \
    -H "Content-Type: application/json" \
    -d '{<key>: <new_value>}' \
    http://localhost/person/<id>

```

```(cmd)
curl -X PUT \
    -H "Content-Type: application/json" \
    -d '{$set : {"sex": "male"}} \
    http://localhost/person/<id>
```
