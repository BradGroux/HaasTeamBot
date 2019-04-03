import datetime
import os

import praw
import requests
import requests.auth

import template


class HaasBotController(object):
    def __init__(self):
        self.reddit_username = os.getenv("REDDIT_USERNAME", "")
        self.reddit_password = os.getenv("REDDIT_PASSWORD", "")
        self.client_token = os.getenv("CLIENT_TOKEN", "")
        self.client_secret = os.getenv("CLIENT_SECRET", "")

    def lookup_current_race(self):
        today = datetime.date.today().isoformat()
        tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).isoformat()

        r = requests.get("http://ergast.com/api/f1/current.json")
        races = r.json()["MRData"]["RaceTable"]

        for race in races["Races"]:
            if race["date"] in [today, tomorrow]:
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

        parsed_template = template

        title = "Test HaasBot Post"
        s = reddit.subreddit("HaasTeamBot").submit(
            title=title, selftext="Test Post from HaasBot"
        )
        return s.url
