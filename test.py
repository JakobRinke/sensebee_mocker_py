import py_sensbee.sensor as sensor
import time

test_id = "5401df3b-9367-4e8b-b2dd-6dba2b6cade6"
s = sensor.Sensor(test_id, read_api_key="ab1920a1-230d-4e93-a923-f2874f59cf97")


d = s.get_data(limit=100, )
print(d)
