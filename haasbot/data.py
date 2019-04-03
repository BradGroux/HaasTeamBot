import datetime

import requests


def get_next_race():
    today = datetime.date.today()
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)

    r = requests.get("http://ergast.com/api/f1/current.json")
    races = r.json()["MRData"]["RaceTable"]

    print(races)

    for race in races["Races"]:
        race_date = datetime.datetime.strptime(race["date"], "%Y-%m-%d")
        print(race_date)


def get_qualifying_results(race_round):
    pass
