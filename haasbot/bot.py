import datetime
import os

import praw

from . import template


class HaasBotController(object):
    def __init__(self, constructor_name):
        self.reddit_username = os.getenv("REDDIT_USERNAME", "")
        self.reddit_password = os.getenv("REDDIT_PASSWORD", "")
        self.client_token = os.getenv("CLIENT_TOKEN", "")
        self.client_secret = os.getenv("CLIENT_SECRET", "")

        # Storing this for now, for use later
        self.constructor_name = constructor_name

        # Some convenience date information
        self.today = datetime.date.today().isoformat()

    def post_race_thread(self, template_file):
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
