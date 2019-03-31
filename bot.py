import os

import praw
import requests
import requests.auth


class HaasBot(object):
    def __init__(self):
        self.reddit_username = os.getenv("REDDIT_USERNAME", "")
        self.reddit_password = os.getenv("REDDIT_PASSWORD", "")
        self.client_token = os.getenv("CLIENT_TOKEN", "")
        self.client_secret = os.getenv("CLIENT_SECRET", "")

    def post_to_subreddit(self):
        # First set up auth
        reddit = praw.Reddit(
            client_id=self.client_token,
            client_secret=self.client_secret,
            password=self.reddit_password,
            username=self.reddit_username,
            user_agent="python:HaasBot:v0.1.0",
        )
        s = reddit.subreddit("HaasTeamBot").submit(
            title="Hello from Gunther Steiner (Test Post)",
            selftext="Test Post from HaasBot",
        )
        print(s.url)


if __name__ == "__main__":
    h = HaasBot()
    h.post_to_subreddit()
