import py_sensbee.sensor as sensor
import time

test_id = "80071a71-9328-4936-8e06-dc134ccd2184"
s = sensor.Sensor(test_id, write_api_key="5e21cd38-caaf-4427-9b04-3b357fba3c36", read_api_key="4a54a59e-abfc-4a26-a21f-5a9695c6cc80")


# s.upload_data([{
#     "temperature": 23.0,
# }])

d = s.get_data(limit=1)
print(d)