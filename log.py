import json
import time

LOG_FILE = "alerts.json"

def log_alert(survivor_id, image_path, lat, lon):
    alert = {
        "id": survivor_id,
        "image": image_path,
        "lat": lat,
        "lon": lon,
        "time": time.strftime("%Y-%m-%d %H:%M:%S")
    }

    try:
        with open(LOG_FILE, "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append(alert)

    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=2)
