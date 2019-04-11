import datetime
import os

import praw

from . import template, race


class HaasBotController(object):
    def __init__(self, constructor_name="Haas"):
        self.reddit_username = os.getenv("REDDIT_USERNAME", "")
        self.reddit_password = os.getenv("REDDIT_PASSWORD", "")
        self.client_token = os.getenv("CLIENT_TOKEN", "")
        self.client_secret = os.getenv("CLIENT_SECRET", "")

        # Storing this for now, for use later
        self.constructor_name = constructor_name

        # Some convenience date information
        self.today = datetime.date.today().isoformat()

    def post_race_thread(self, race_type=None):
        # First set up auth
        reddit = praw.Reddit(
            client_id=self.client_token,
            client_secret=self.client_secret,
            password=self.reddit_password,
            username=self.reddit_username,
            user_agent="python:HaasBot:v0.1.0",
        )

        # Getting the next race and posting about it
        r = race.Race()
        race_name = r.name
        race_date_range_string = r.race_weekend_range()
        race_location = r.location
        circuit_name = r.circuit_name
        race_url = r.circuit_url

        # Random stuff for timezones
        all_timezones = r.get_start_all_timezones()
        start_all_timezones = []
        for timezone, time in all_timezones.items():
            start_all_timezones.append(time)

        parsed_template = template.load_template_file(
            "race.tmpl",
            race_name=race_name,
            race_date_range_string=race_date_range_string,
            race_location=race_location,
            circuit_name=circuit_name,
            race_url=race_url,
            start_all_timezones=start_all_timezones,
        )

        title = f"Test HaasBot Race Thread: {self.today}"
        s = reddit.subreddit("HaasTeamBot").submit(
            title=title, selftext=parsed_template
        )
        return s.url
