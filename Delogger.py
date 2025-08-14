import requests
import json
import time
from datetime import datetime, timezone

# ─── Configuration ──────────────────────────────────────────────
API_KEY = "5a758b336f87fc68dc1a74502d7f56fcd51f334fc6b533520a668c62fdd945d8"

NODES_VARIABLES = {
    "0198504f-33eb-7166-a1aa-828b476327e1": "temperature",
    "01985045-58ea-7ae9-932f-825381cccc50": "humidity",
    "01985046-6440-79ae-a21e-994f04f2dfc1": "SoilMoisture",
    "01985046-bd70-7d43-b38b-5792e0dd43be": "UVINDEX",
    "01985045-def6-7379-a7ea-309113ee6f66": "AQI"
}

LIMIT = 1
ORDER = "desc"
POLL_INTERVAL = 5     # seconds
WINDOW_SIZE   = 60    # seconds

URL = "https://api.ap-in-1.anedya.io/v1/data/getData"
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

# ─── Helper: Parse timestamp safely ─────────────────────────────
def parse_timestamp(ts):
    try:
        if isinstance(ts, str):
            if ts.isdigit():
                ts = int(ts)
            else:
                dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
                return int(dt.timestamp())
        elif isinstance(ts, (int, float)):
            ts = int(ts)
        if ts > 1e12:  # if in milliseconds
            ts = ts // 1000
        return ts
    except Exception:
        return None

# ─── Main Loop ──────────────────────────────────────────────────
print("🔄 Real-time sensor fetcher started...\n")

while True:
    to_time = int(time.time())
    from_time = to_time - WINDOW_SIZE

    for node_id, variable in NODES_VARIABLES.items():
        payload = {
            "variable": variable,
            "nodes": [node_id],
            "from": from_time,
            "to": to_time,
            "limit": LIMIT,
            "order": ORDER
        }

        try:
            response = requests.post(URL, headers=HEADERS, data=json.dumps(payload), timeout=10)

            if response.status_code != 200:
                print(f"❌ HTTP {response.status_code} for {variable}@{node_id}: {response.text}")
                continue

            result = response.json()
            if not result.get("success", False):
                print(f"❌ API Error for {variable}@{node_id}: {result.get('error', 'Unknown')}")
                continue

            raw_data = result.get("data", [])
            records = []

            # Handle both dict and list responses
            if isinstance(raw_data, list):
                records = raw_data
            elif isinstance(raw_data, dict):
                for v in raw_data.values():
                    if isinstance(v, list):
                        records.extend(v)

            if not records:
                print(f"[{datetime.utcnow():%H:%M:%S} GMT] No data for {variable}@{node_id} in last {WINDOW_SIZE}s.")
                continue

            record = records[0]
            ts_raw = record.get("timestamp") or record.get("ts")
            ts_parsed = parse_timestamp(ts_raw)

            if ts_parsed is None:
                print(f"⚠️ Invalid timestamp for {variable}@{node_id}")
                continue

            dt = datetime.fromtimestamp(ts_parsed, tz=timezone.utc)
            value = record.get("value", "N/A")

            print(f"{dt:%Y-%m-%d %H:%M:%S} GMT → {variable}@{node_id}: {value}")

        except requests.exceptions.RequestException as e:
            print(f"❌ Request failed for {variable}@{node_id}: {e}")

    time.sleep(POLL_INTERVAL)
