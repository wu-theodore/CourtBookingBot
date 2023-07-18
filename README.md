# CourtBookingBot
Simple bot to fight for a badminton court at UofT. Works by opening a scripted browser and simulates user actions.

The bot should be run at least tw days in advance of the desired date (since courts are tight).

## Setup
The bot was developed with Python 3. Be sure to import the necessary packages with `pip install -r requirements.txt`

## Usage
Run `main.py` with the following arguments:
- **-d/--date**: Datetime string of format DD/MM/YYYY.
- **-t/--time**: 24hr format hour integer, two digit (HH).
- **-n/--num**: Which court number to try and book {1, 2, 3}.
- **-u/--username**: UTORID username.
- **-p/--password**: Password associated with UTORID.

Use flag "-h" for command-line help (`python main.py -h`)
