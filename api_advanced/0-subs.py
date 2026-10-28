#!/usr/bin/python3
"""Query the Reddit API for a subreddit's subscriber count."""

import requests


HEADERS = {"User-Agent": "api_advanced/1.0 (by u/cniyonkuru1-jpg)"}


def number_of_subscribers(subreddit):
    """Return the subscriber count for subreddit, or 0 when it is invalid."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=HEADERS, allow_redirects=False)

    if response.status_code != 200:
        return 0
    return response.json().get("data").get("subscribers")
