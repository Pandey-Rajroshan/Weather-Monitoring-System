import requests
import random
import time
from datetime import datetime, timezone

# ─── Nodes Configuration (now each will get all variables) ──────────────────
nodes = [
    {
        "name": "Temperature",
        "nodeId": "0198504f-33eb-7166-a1aa-828b476327e1",
        "connectionKey": "10bca7d8e9da7835972e7dcaee3d9fc3"
    },
    {
        "name": "Humidity",
        "nodeId": "01985045-58ea-7ae9-932f-825381cccc50",
        "connectionKey": "5931a16abc5cc9042ba123322602bc27"
    },
    {
        "name": "SoilMoisture",
        "nodeId": "01985046-6440-79ae-a21e-994f04f2dfc1",
        "connectionKey": "655f9879ecd70c9c1b564b3eea5d51c3"
    },
    {
        "name": "UVINDEX",
        "nodeId": "01985046-bd70-7d43-b38b-5792e0dd43be",
        "connectionKey": "d4ec18e66266733cd5b11e28061e5db5"
    },
    {
        "name": "AQI",
        "nodeId": "01985045-def6-7379-a7ea-309113ee6f66",
        "connectionKey": "2da96083c7678574310d88c8b96dc442"
    }
]

URL = "https://device.ap-in-1.anedya.io/v1/submitData"

# ─── Function to generate all variable values ──────────────────────────────
def generate_variable_data():
    return [
        {"variable": "temperature", "value": round(random.uniform(20, 40), 2)},
        {"variable": "humidity", "value": round(random.uniform(30, 90), 2)},
        {"variable": "SoilMoisture", "value": round(random.uniform(10, 60), 2)},
        {"variable": "UVINDEX", "value": round(random.uniform(0, 12), 2)},
        {"variable": "AQI", "value": round(random.uniform(50, 300), 2)}
    ]

# ─── Function to send data to a node ───────────────────────────────────────
def send_data_to_node(node):
    payload = {
        "nodeId": node["nodeId"],
        "data": generate_variable_data()
    }

    headers = {
        "Auth-mode": "key",
        "Authorization": node["connectionKey"],
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    now_utc = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S GMT')

    try:
        response = requests.post(URL, headers=headers, json=payload, timeout=10)
        response.raise_for_status()
        print(f"✅ {now_utc} | {node['name']} → {response.json()}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error sending to {node['name']}: {e}")

# ─── Main Loop ────────────────────────────────────────────────────────────
try:
    while True:
        print("\n🚀 Sending all variables to all nodes...")
        for node in nodes:
            send_data_to_node(node)
        time.sleep(5)
except KeyboardInterrupt:
    print("\n🛑 Script stopped by user.")
