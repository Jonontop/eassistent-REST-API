# Eassistent urnik izpis

## Code
```py
import requests
from bs4 import BeautifulSoup
import time

urnik = {
    "1": 7.30,
    "2": 8.20,
    "3": 9.10,
    "4": 10.00,
    "5": 11.05,
    "6": 11.55,
    "7": 12.45,
    "8": 13.35,
    "9": 14.25
}
def curent_date():
    month = f"{time.gmtime()[1]}"
    if len(month) == 1:
        month = f"0{time.gmtime()[1]}"
    day = f"{time.gmtime()[2]}"
    if len(day) == 1:
        day = f"0{time.gmtime()[2]}"

    return f"{time.gmtime()[0]}-{month}-{day}"
# returns the current date in the format "YYYY-MM-DD"

def current_time():
    hour = f"{time.gmtime()[3]}"
    hour = str(int(float(hour)+2))
    if len(hour) == 1:
        hour = f"0{time.gmtime()[3]}"
    minute = f"{time.gmtime()[4]}"
    if len(minute) == 1:
        minute = f"0{time.gmtime()[4]}"
    return float(f"{hour}.{minute}")
# returns the current time in the format "HH.MM"


def eassistent():
    sez = []
    tmp = {}
    url = f"https://www.easistent.com/urniki/30a1b45414856e5598f2d137a5965d5a4ad36826/razredi/541930" # Url of School schedule
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    print()

    for i in range(1, 10):
        results = soup.find_all("td", id=f"ednevnik-seznam_ur_teden-td-{i}-{curent_date()}") # Find all the subjects for the current day

        for j in results:
            try:
                name = j.find("td", class_="text14 bold").text # Name of the subject
                prof = j.find("div", class_="text11").text.index(",") # Index of the comma in the text
                prof = j.find("div", class_="text11").text[0:prof] # Name of the professor
                room = j.find("div", class_="text11").text.index(",") # Index of the comma in the text
                room = j.find("div", class_="text11").text[room + 2:] # Room of the subject
                tmp = {
                    "name": name.strip(),
                    "prof": prof.strip(),
                    "room": room.strip(),
                    "time": f"{i}. ura",
                    "group": j.find_all("div", class_="text11 gray bold")[0].text if j.find_all("div", class_="text11 gray bold") else None
                }
                sez.append(tmp)

            except:
                pass

    if sez == []:
        return "Ni pouka, vikend"
    return sez

# print(eassistent())


def easistent_current_hour():
    thresholds = [8.20, 9.10, 10.00, 11.05, 11.55, 12.45, 13.35, 14.25]
    current = current_time()
    for i, threshold in enumerate(thresholds, start=1):
        if current < threshold:
            return i
    return len(thresholds) + 1

print(eassistent())

```

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

