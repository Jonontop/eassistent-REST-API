# Eassistent urnik izpis



- koda je bila narejen v mojem prostem času

School Schedule Scraper
=======================

This Python script fetches and parses the daily schedule from the eAsistent platform for a specific school and date.

Prerequisites
-------------

Make sure you have the following Python packages installed:
- `requests`
- `beautifulsoup4`

You can install them using pip:
pip install requests beautifulsoup4


Functions
---------

### `curent_date()`

Returns the current date in the format "YYYY-MM-DD".

Usage example:
from your_module import curent_date

current_date = curent_date()
print(f"Current date: {current_date}")


### `current_time()`

Returns the current time in the format "HH.MM".

Usage example:
from your_module import current_time

current_time = current_time()
print(f"Current time: {current_time}")


### `eassistent()`

Fetches the daily school schedule from eAsistent for a specific URL and date.
Returns a list of dictionaries containing schedule details like subject name, professor, room, time, and group.

Usage example:
from your_module import eassistent

schedule = eassistent()
for lesson in schedule:
print(f"Subject: {lesson['name']}, Professor: {lesson['prof']}, Room: {lesson['room']}, Time: {lesson['time']}, Group: {lesson['group']}")


### `easistent_current_hour()`

Determines the current hour of the school day based on the current time.
Returns the current hour number or the next hour if it's between periods.

Usage example:
from your_module import easistent_current_hour

current_hour = easistent_current_hour()
print(f"Current school hour: {current_hour}")


Notes
-----

- Replace the `url` variable in the `eassistent()` function with the correct URL for your school's schedule.
- The script currently prints the schedule to the console. Modify it to suit your specific needs (e.g., store in a database, send notifications, etc.).

