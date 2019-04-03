import datetime
import os

import praw
import requests
import requests.auth


class HaasBotController(object):
    def __init__(self):
        self.reddit_username = os.getenv("REDDIT_USERNAME", "")
        self.reddit_password = os.getenv("REDDIT_PASSWORD", "")
        self.client_token = os.getenv("CLIENT_TOKEN", "")
        self.client_secret = os.getenv("CLIENT_SECRET", "")

    def lookup_current_race(self):
        test = datetime.date(2019, 4, 28).isoformat()
        tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).isoformat()

        r = requests.get("http://ergast.com/api/f1/current.json")
        races = r.json()["MRData"]["RaceTable"]

        for race in races["Races"]:
            if race["date"] in [test, tomorrow]:
                return race

    def get_qualifying_results(self, race_round):
        pass

    def post_to_subreddit(self, message):
        # First set up auth
        reddit = praw.Reddit(
            client_id=self.client_token,
            client_secret=self.client_secret,
            password=self.reddit_password,
            username=self.reddit_username,
            user_agent="python:HaasBot:v0.1.0",
        )
        s = reddit.subreddit("HaasTeamBot").submit(
            title=message, selftext="Test Post from HaasBot"
        )
        return s.url
