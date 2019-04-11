import maya
import requests

from collections import OrderedDict


class Race(object):
    def __init__(self):
        self.init_next_race()

    def init_next_race(self):
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

        # Setting some pieces of information we will want for later
        self.round = next_race["round"]
        self.name = next_race["raceName"]
        self.location = next_race["Circuit"]["Location"]["locality"]
        # Converting returned url to https because it's 2019
        self.circuit_name = next_race["Circuit"]["circuitName"]
        self.circuit_url = next_race["Circuit"]["url"].replace("http", "https")

        # Obtaining a 'raw' maya datetime object for the race start datetime
        race_datetime = maya.parse(
            f"{next_race['date']} {next_race['time']}", timezone="ETC/Zulu"
        )
        self.race_datetime = race_datetime

    def race_weekend_range(self):
        # We know a race weekend always (I think) starts two days before the race date
        race_weekend_start = self.race_datetime.subtract(days=2)
        start_string = race_weekend_start.datetime().strftime("%a %d %h")
        end_string = self.race_datetime.datetime().strftime("%a %d %h")
        return f"{start_string} - {end_string}"

    def get_start_all_timezones(self):
        timezones = {
            "utc": "UTC",
            "est": "US/Eastern",
            "cst": "US/Central",
            "mst": "US/Mountain",
            "pst": "US/Pacific",
        }

        # Empty dict we will populate with the race's start time for each time-zone we want
        start_all_timezones = OrderedDict()

        for short_name, full_name in timezones.items():
            time = self.race_datetime.datetime(to_timezone=full_name).strftime(
                "%d %b %H:%M"
            )
            start_all_timezones[short_name] = time

        return start_all_timezones
