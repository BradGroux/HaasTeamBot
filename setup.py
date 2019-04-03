# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open("readme.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="HaasBot",
    version="0.1.0",
    description="Reddit Bot for Formula 1 Subreddit Management",
    long_description=readme,
    author="Julian Gindi",
    author_email="julian@gindi.io",
    url="https://github.com/BradGroux/HaasTeamBot",
    license=license,
    packages=find_packages(exclude=("tests", "docs")),
)
