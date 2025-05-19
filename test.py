import py_sensbee.sensor as sensor
import time

test_id = "c359f1e8-0493-4cd6-945b-db690760a22c"
s = sensor.Sensor(test_id, read_api_key="6849fe40-95a8-447e-bf6f-9e08b35c3f6c")


# s.upload_data([{
#     "temperature": 23.0,
# }])

d = s.get_data(limit=5)
print(d)