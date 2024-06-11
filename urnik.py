import requests
from bs4 import BeautifulSoup
import time

def curent_date():
    month = f"{time.gmtime()[1]}"
    if len(month) == 1:
        month = f"0{time.gmtime()[1]}"
    day = f"{time.gmtime()[2]}"
    if len(day) == 1:
        day = f"0{time.gmtime()[2]}"
    return f"2024-06-12"
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
        print(type(results))
        for j in results:
            try:
                print(j)
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

urnik = eassistent()
for i in urnik:
    print(i)

