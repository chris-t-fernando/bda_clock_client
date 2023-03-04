import requests
from datetime import datetime
from . import config


class ClockCreateFailed(Exception):
    ...


def has_clock(id: str):
    url = f"{config.urlbase}{id}"
    response = requests.get(url)
    clock_exists = response.status_code >= 200 and response.status_code < 300
    return clock_exists


def make_clock(id: str, start: datetime, interval_seconds: int):
    url = f"{config.urlbase}"
    myobj = {"id": id, "interval": interval_seconds, "start": str(start)}
    response = requests.post(url, json=myobj)
    error = response.status_code < 200 or response.status_code >= 300
    if error:
        raise ClockCreateFailed(response)

    return response
