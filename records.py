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

def average_rating_by_language(records):
    """Calculate the average show rating for each language"""
    ratings_by_language = {}

    for show in records:
        language = show.get("language")
        rating_data = show.get("rating") or {}
        rating = rating_data.get("average")

        if not language or rating is None:
            continue

        if language not in ratings_by_language:
            ratings_by_language[language] = []

        ratings_by_language[language].append(rating)

    return {
        language: round(sum(ratings) / len(ratings), 2)
        for language, ratings in ratings_by_language.items()
    }


def main():
    try:
        records = fetch_records(source_url)

    except (requests.RequestException, ValueError) as error:
        print(f"Could not download TV show data: {error}")
        return

    print(f"Downloaded {len(records)} records from {source_url}")
    print(f"Summary written to {output}")


if __name__ == "__main__":
    main()
