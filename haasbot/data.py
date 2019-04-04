import datetime

import requests


def get_next_race():
    today = datetime.date.today()

    r = requests.get("http://ergast.com/api/f1/current.json")
    races = r.json()["MRData"]["RaceTable"]

    for race in races["Races"]:
        race_date = datetime.date.fromisoformat(race["date"])
        if today > race_date:
            continue
        else:
            return race


def get_qualifying_results(race_round):
    pass
