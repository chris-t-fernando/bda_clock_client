import requests
from datetime import datetime

# from .config import urlbase
from .config import *
import json


class BdaClock:
    id: str
    start: datetime
    now: datetime
    interval: int

    def __init__(self, id: str):
        self.id = id
        response = requests.get(f"{urlbase}{id}")
        response_json = json.loads(response.text)
        self.now = response_json["now"]
        self.start = response_json["start"]
        self.interval = response_json["interval"]

    def tick(self):
        url = f"{urlbase}{self.id}/tick"
        response = requests.put(url)
        response_json = json.loads(response.text)
        self.now = response_json["now"]
        return self.now

    def reset(self):
        url = f"{urlbase}{self.id}/reset"
        response = requests.put(url)
        response_json = json.loads(response.text)
        self.now = response_json["now"]
        return self.now
