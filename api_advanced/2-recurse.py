#!/usr/bin/python3
"""Recursively collect all hot-post titles for a subreddit."""

import requests


HEADERS = {"User-Agent": "api_advanced/1.0 (by u/cniyonkuru1-jpg)"}


def recurse(subreddit, hot_list=None, after=None):
    """Return every hot-post title for subreddit, or None if it is invalid."""
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(
        url, headers=HEADERS, params={"after": after}, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data")
    titles = [post.get("data").get("title")
              for post in data.get("children")]
    hot_list.extend(titles)
    after = data.get("after")
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
