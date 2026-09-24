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

def shows_per_genre(records):
    """Count how many shows belong to each genre."""
    genre_shows_count = {}

    for show in records:
        genres = show.get("genres") or []

        for genre in genres:
            genre_shows_count[genre] = genre_shows_count.get(genre, 0) + 1

    return genre_shows_count

def main():
    records = fetch_records(source_url)
    print(f"\nDownloaded {len(records)} records from {source_url}")
    
    print("\nCount how many shows belong to each genre")
    genre_shows_count = shows_per_genre(records)
    for genre, count in genre_shows_count.items():
        print(f"{genre}: {count}")

if __name__ == "__main__":
    main()
