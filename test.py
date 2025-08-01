import py_sensbee.sensor as sensor
import time

test_id = "64c3f9f9-06e5-451e-b472-e4dee929c59e"
s = sensor.Sensor(test_id, read_api_key="3eba757e-39b5-455a-9be1-338706a80f41")
d = s.get_data(limit=100, )
print(d)