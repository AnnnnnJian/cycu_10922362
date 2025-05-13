import requests
import pandas as pd
import os

def fetch_bus_data(route_id):
    url = f"https://ebus.gov.taipei/Route/StopsOfRoute?routeid={route_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def parse_bus_data(data):
    try:
        stops = data.get('Stops', [])
        parsed_data = []
        for stop in stops:
            parsed_data.append({
                '車到達時間': stop.get('arrival_info', '未知'),
                '車站序號': stop.get('stop_number', '未知'),
                '車站名稱': stop.get('stop_name', '未知'),
                '車站編號': stop.get('stop_id', '未知'),
                'latitude': stop.get('latitude', '未知'),
                'longitude': stop.get('longitude', '未知')
            })
        return parsed_data
    except Exception as e:
        print(f"Error parsing data: {e}")
        return []

def save_to_csv(data, route_id):
    if not os.path.exists('data'):
        os.makedirs('data')

    file_path = f"data/bus_route_{route_id}.csv"
    try:
        df = pd.DataFrame(data)
        df.to_csv(file_path, index=False, encoding='utf-8-sig')
        print(f"資料已成功輸出至 {file_path}")
    except Exception as e:
        print(f"Error saving to CSV: {e}")

def main():
    route_id = "10100000A00"  # Example route ID
    data = fetch_bus_data(route_id)
    if data:
        parsed_data = parse_bus_data(data)
        save_to_csv(parsed_data, route_id)

if __name__ == "__main__":
    main()