# Ical to JSON converter

Fetch events from iCalendar, including recurring events.

## Setup

    python3 -m venv .venv
    . .venv/bin/activate
    pip install -r requirements.txt

## Usage

    python ical_to_json.py --start=2017-05-18 --days=6 https://github.com/irgangla/icalevents/raw/master/test/test_data/basic.ics
