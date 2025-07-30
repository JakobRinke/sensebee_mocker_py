import requests
import config

class Sensor:
    def __init__(self, id:str, write_api_key:str=None, read_api_key:str=None):
        self.id = id
        self.write_api_key = write_api_key
        self.read_api_key = read_api_key
    
    def upload_data(self, data:dict):
        """
        Uploads data to the server.
        """
        url = f"{config.SENSBEE_API_URL}/data/sensor/{self.id}/ingest?key={self.write_api_key}"
        resp = requests.post(
            url,
            json=data
        )

        if resp.status_code != 200:
            raise Exception(f"Failed to upload data: {resp.status_code} {resp.text}")
        return resp.json()
    
    def get_data(self, start_time=None, end_time=None, limit=None, ordering="ASC"):

        url = f"{config.SENSBEE_API_URL}/data/sensor/{self.id}/load?key={self.read_api_key}"
        if start_time is not None:
            url += f"&start_time={start_time}"
        if end_time is not None:
            url += f"&end_time={end_time}"
        if limit is not None:
            url += f"&limit={limit}"
        if ordering is not None:
            url += f"&ordering={ordering}"

        resp = requests.get(url)

        if resp.status_code != 200:
            raise Exception(f"Failed to get data: {resp.status_code} {resp.text}")
        return resp.json()
