import datetime
import os

import praw
import requests
import requests.auth

from . import template


class HaasBotController(object):
    def __init__(self):
        self.reddit_username = os.getenv("REDDIT_USERNAME", "")
        self.reddit_password = os.getenv("REDDIT_PASSWORD", "")
        self.client_token = os.getenv("CLIENT_TOKEN", "")
        self.client_secret = os.getenv("CLIENT_SECRET", "")

        # Some convenience date information
        self.today = datetime.date.today().isoformat()
        self.tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).isoformat()

    def lookup_current_race(self):
        r = requests.get("http://ergast.com/api/f1/current.json")
        races = r.json()["MRData"]["RaceTable"]

        for race in races["Races"]:
            if race["date"] in [self.today, self.tomorrow]:
                return race

    def get_qualifying_results(self, race_round):
        pass

    def post_to_subreddit(self, template_file):
        # First set up auth
        reddit = praw.Reddit(
            client_id=self.client_token,
            client_secret=self.client_secret,
            password=self.reddit_password,
            username=self.reddit_username,
            user_agent="python:HaasBot:v0.1.0",
        )

        parsed_template = template.load_template_file(
            template_file, test_variable="Hello World"
        )

        title = f"Test HaasBot Post: {self.today}"
        s = reddit.subreddit("HaasTeamBot").submit(
            title=title, selftext=parsed_template
        )
        return s.url
