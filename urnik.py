import requests
from bs4 import BeautifulSoup
import time

# returns the current date in the format "YYYY-MM-DD"
curent_date = lambda: time.strftime("%Y-%m-%d", time.gmtime())

# returns the current time in the format "HH:MM"
current_time = lambda: float(time.strftime("%H.%M", time.gmtime()))


def eassistent():
    sez = []
    url = f"https://www.easistent.com/urniki/30a1b45414856e5598f2d137a5965d5a4ad36826/razredi/639511"  # Url of School schedule
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    print()

    for i in range(1, 10):
        results = soup.find_all("td", id=f"ednevnik-seznam_ur_teden-td-{i}-{curent_date()}")  # Find all the subjects for the current day
        print(type(results))
        for j in results:
            try:
                print(j)
                name = j.find("td", class_="text14 bold").text  # Name of the subject
                prof = j.find("div", class_="text11").text.index(",")  # Index of the comma in the text
                prof = j.find("div", class_="text11").text[0:prof]  # Name of the professor
                room = j.find("div", class_="text11").text.index(",")  # Index of the comma in the text
                room = j.find("div", class_="text11").text[room + 2:]  # Room of the subject
                tmp = {
                    "name": name.strip(),
                    "prof": prof.strip(),
                    "room": room.strip(),
                    "time": f"{i}. ura",
                    "group": j.find_all("div", class_="text11 gray bold")[0].text if j.find_all("div", class_= "text11 gray bold") else None
                }
                sez.append(tmp)

            except:
                pass

    return "Ni pouka, vikend" if sez == [] else sez


# print(eassistent())


def easistent_current_hour():
    thresholds = [8.20, 9.10, 10.00, 11.05, 11.55, 12.45, 13.35, 14.25]
    current = current_time()
    for i, threshold in enumerate(thresholds, start=1):
        if current < threshold:
            return i
    return len(thresholds) + 1


[print(i) for i in eassistent()]
