#!/usr/bin/python3
"""Recursively count requested words in a subreddit's hot-post titles."""

import requests


HEADERS = {"User-Agent": "api_advanced/1.0 (by u/cniyonkuru1-jpg)"}


def count_words(subreddit, word_list, counts=None, multiples=None, after=None):
    """Print sorted case-insensitive counts for a subreddit's hot posts."""
    if counts is None:
        counts = {}
        multiples = {}
        for word in word_list:
            word = word.lower()
            counts[word] = 0
            multiples[word] = multiples.get(word, 0) + 1

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(
        url, headers=HEADERS, params={"after": after}, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get("data")
    for post in data.get("children"):
        title = post.get("data").get("title").lower().split()
        for word in title:
            if word in counts:
                counts[word] += multiples.get(word)

    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, counts, multiples, after)

    ordered_counts = sorted(
        counts.items(), key=lambda item: (-item[1], item[0]))
    for word, total in ordered_counts:
        if total:
            print("{}: {}".format(word, total))
