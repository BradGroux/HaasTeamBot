import maya
import requests


class Race(object):
    def __init__(self):
        self.get_next_race()

    def get_next_race(self):
        """ Sets the Race object's metadata according to the upcoming race """
        now = maya.now()

        r = requests.get("http://ergast.com/api/f1/current.json")
        races = r.json()["MRData"]["RaceTable"]
        next_race = None

        for race in races["Races"]:
            race_date = maya.parse(race["date"])
            if now < race_date:
                next_race = race
                break
            else:
                continue

        self.round = next_race["round"]
        self.name = next_race["raceName"]

        race_datetime = maya.parse(f"{next_race['date']} {next_race['time']}")
        self.race_datetime = race_datetime

    def race_weekend_range(self):
        # We know a race weekend always (I think) starts two days before the race date
        race_weekend_start = self.race_datetime.subtract(days=2)
        start_string = race_weekend_start.datetime().strftime("%a %d %h")
        end_string = self.race_datetime.datetime().strftime("%a %d %h")
        return f"{start_string} - {end_string}"
