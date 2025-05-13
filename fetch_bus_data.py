import requests
import pandas as pd
import csv
import os
from playwright.sync_api import sync_playwright

# Ensure the 'data' directory exists
if not os.path.exists('data'):
    os.makedirs('data')

def fetch_bus_data_with_playwright(route_id):
    """
    Fetch bus data using Playwright and save it as a CSV file.

    Args:
        route_id (str): The bus route ID to fetch data for.
    """
    url = f"https://ebus.gov.taipei/Route/StopsOfRoute?routeid={route_id}"
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url)
            content = page.content()
            browser.close()

        # Parse JSON from the page content
        data = requests.get(url, verify=False).json()
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

        # Save to CSV
        file_path = f"data/bus_route_{route_id}.csv"
        df = pd.DataFrame(parsed_data)
        df.to_csv(file_path, index=False, encoding='utf-8-sig')
        print(f"資料已成功輸出至 {file_path}")

    except Exception as e:
        print(f"Error fetching or processing data: {e}")

# Example usage
if __name__ == "__main__":
    fetch_bus_data_with_playwright("0100000A00")