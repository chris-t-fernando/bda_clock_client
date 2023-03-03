from bda_clock import client
from datetime import datetime
import json

if client.has_clock("banana"):
    print(f"Clock named banana exists")
else:
    print(f"Clock named banana does not exist - trying to make it...")
    try:
        new_clock = client.make_clock(
            id="banana", start=datetime.now().astimezone(), interval_seconds=300
        )
    except client.ClockCreateFailed as e:
        print(f"Failed to create new clock. Error: {str(e)}")
    else:
        json_clock = json.loads(new_clock.text)
        print(f"Created clock {json_clock['id']}")

if client.has_clock("clock1"):
    print(f"Clock named clock1 exists")
else:
    print(f"Clock named clock1 does not exist")
