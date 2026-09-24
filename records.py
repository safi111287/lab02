import json
import requests

from pathlib import Path

source_url = "https://api.tvmaze.com/shows?page=0"
output = Path("summary.json")

def fetch_records(url):
    """Download TV show records and return them as Python objects"""
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()

def main():
    records = fetch_records(source_url)
    print(f"Downloaded {len(records)} records from {source_url}")

if __name__ == "__main__":
    main()
