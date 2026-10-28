#!/usr/bin/python3
"""Print the titles of a subreddit's first ten hot posts."""

import requests


HEADERS = {"User-Agent": "api_advanced/1.0 (by u/cniyonkuru1-jpg)"}


def top_ten(subreddit):
    """Print ten hot-post titles for subreddit, or None when it is invalid."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers=HEADERS, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    posts = response.json().get("data").get("children")
    for post in posts[:10]:
        print(post.get("data").get("title"))
