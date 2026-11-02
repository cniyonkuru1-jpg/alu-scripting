#!/usr/bin/python3
"""Print the titles of a subreddit's first ten hot posts."""

import requests


HEADERS = {"User-Agent": "api_advanced/1.0 (by u/cniyonkuru1-jpg)"}


def top_ten(subreddit):
    """Print ten hot-post titles for subreddit, or None when it is invalid."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers=HEADERS, allow_redirects=False)

    try:
        payload = response.json()
    except ValueError:
        print(None)
        return None

    if not isinstance(payload, dict):
        print(None)
        return None

    data = payload.get("data")
    if not isinstance(data, dict):
        print(None)
        return None

    posts = data.get("children")
    if not isinstance(posts, list):
        print(None)
        return None

    for post in posts[:10]:
        if not isinstance(post, dict):
            continue
        post_data = post.get("data")
        if isinstance(post_data, dict) and "title" in post_data:
            print(post_data["title"])
