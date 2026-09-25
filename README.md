# Lab 02 - TV Show Aggregation Program

This program downloads real TV show records from the public TVMaze API, summarizes the data using several aggregations, and writes the results to a JSON file. It also handles missing or inconsistent values without crashing.

## Data Source

The program uses the TVMaze public API:

https://api.tvmaze.com/shows?page=0

Each record represents one TV show and includes information such as the show name, language, genres, rating, network, and premiere date.

At the time of testing, the API returned approximately 240 records. The number may change if the source data is updated.

## Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/safi111287/lab02.git test-lab02-clone
```

Then move into the project folder:

```bash
cd test-lab02-clone
```

## Setup

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate it

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```
If PowerShell blocks script execution, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
Then activate the environment again with the same command
```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## Run

Run the program with:

```bash
python records.py
```

The program downloads the TV show records, performs the aggregations, and creates or updates the `summary.json` file.

## Example Output

Example terminal output:

```text
Downloaded 240 records from https://api.tvmaze.com/shows?page=0

Summary of TV show data: {'source_url': 'https://api.tvmaze.com/shows?page=0', 'records_processed': 240, 'shows_per_genre': {'Drama': 154, 'Science-Fiction': 39, 'Thriller': 41, 'Action': 55, 'Crime': 57, 'Horror': 21, 'Romance': 32, 'Adventure': 23, 'Espionage': 2, 'Music': 3, 'Mystery': 15, 'Supernatural': 18, 'Fantasy': 13, 'Family': 21, 'Anime': 4, 'Comedy': 66, 'History': 4, 'Medical': 6, 'Legal': 6, 'Western': 3, 'War': 4, 'Sports': 2}, 'average_rating_by_language': {'English': 7.58, 'Japanese': 7.88}, 'shows_per_network': {'CBS': 28, 'CTV Sci-Fi Channel': 2, 'The CW': 13, 'HBO': 15, 'Paramount+ with Showtime': 14, 'FOX': 23, 'ABC': 27, 'NBC': 26, 'Showcase': 2, 'FX': 9, 'TNT': 5, 'Fuji TV': 1, 'TBS': 2, 'NTV': 2, 'History': 1, 'No Network': 11, 'Syfy': 13, 'AMC': 5, 'BBC America': 1, 'STARZ': 4, 'Lifetime': 3, 'Cinemax': 2, 'CMT': 1, 'Channel 4': 1, 'A&E': 2, 'USA Network': 4, 'VH1': 1, 'El Rey Network': 1, 'Comedy Central': 3, 'Disney XD': 1, 'MTV': 2, 'Freeform': 4, 'Nickelodeon': 1, 'NewsNation': 1, 'BBC One': 1, 'Audience Network': 1, 'Adult Swim': 1, 'TF1': 1, 'SundanceTV': 1, 'ITV1': 1, 'CBC': 1, 'BBC Two': 1, 'RTL': 1}, 'shows_per_decade': {'2010s': 179, '2000s': 51, '1990s': 8, '1980s': 2}, 'data_quirks': {'shows_without_genres': 5, 'shows_without_rating': 4, 'shows_without_network': 11, 'shows_without_premiered_date': 0, 'unique_languages': ['English', 'Japanese']}}

Summary written to summary.json
```

A short example from `summary.json`:

```json
{
  "source_url": "https://api.tvmaze.com/shows?page=0",
  "records_processed": 240,
  "shows_per_genre": {
    "Drama": 154,
    "Science-Fiction": 39,
    "Thriller": 41,
    "Action": 55,
  },
  "average_rating_by_language": {
    "English": 7.58,
    "Japanese": 7.88
  },
}
```
This is a short example from the complete summary.json file. The full output also includes aggregations by network and decade, as well as data quality information.

The output shows how many records were processed and summarizes the TV shows by genre and average rating by language.  
The complete JSON file also contains network, decade, and data-quality information.

## Data Quirks

The TVMaze data contains several irregularities that the program needs to handle:

- A TV show can belong to several genres. The program loops through all genres for each show, so one show may be counted in more than one genre.
- Some shows have no genres. In the current data, 5 shows have an empty genre list. These records are skipped when counting shows by genre.
- Some shows have no average rating. In the current data, 4 shows have a missing rating. These values are skipped instead of being counted as zero because that would incorrectly lower the average.
- Some shows have no network information. In the current data, 11 shows have no network. These shows are grouped under `"No Network"`.
- Premiere dates may be missing or malformed. The decade aggregation checks the value before using it. In the current dataset, no shows were missing a premiere date.
- The current records contain English and Japanese as the unique languages found by the program.

## Design Choices

The program is divided into small functions so that each function performs one main task. This makes the code easier to understand, test, and modify.

Several Python collection types are used for different purposes:

- **List:** The API response is stored as a list of TV show records. Lists are also used to collect ratings for each language.
- **Dictionary:** Dictionaries are used for grouped results such as shows per genre, network, and decade because they allow each category to be connected to its count or value.
- **Set:** A set is used to collect unique languages because it automatically prevents duplicate values.

A dictionary comprehension is used when calculating the average rating for each language.

The program keeps downloading, aggregation, summary creation, and JSON writing in separate functions rather than combining everything into one large function.

The `pathlib` module is used to manage the `summary.json` output file, and the file is written using UTF-8 encoding and formatted with an indentation of two spaces.

## Known Limitations

- The program currently processes only page 0 of the TVMaze shows API rather than all available pages.
- The program requires an internet connection to download the records.
- Results may change over time because the API contains live public data.
- Shows without an average rating are excluded from the rating calculation.
- Shows without a traditional network are grouped under `"No Network"`.
- The program summarizes the available records but does not attempt to correct information provided by the source API.

## Deactivate the Virtual Environment

When finished, deactivate the virtual environment with:

```bash
deactivate
```