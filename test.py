import py_sensbee.sensor as sensor
import time

# test_id = "5401df3b-9367-4e8b-b2dd-6dba2b6cade6"
# s = sensor.Sensor(test_id, read_api_key="ab1920a1-230d-4e93-a923-f2874f59cf97")

test_id = "64c3f9f9-06e5-451e-b472-e4dee929c59e"
s = sensor.Sensor(test_id, read_api_key="3eba757e-39b5-455a-9be1-338706a80f41")

d = s.get_data(limit=100, )
print(d)
