# API advanced

This project uses the Reddit API to retrieve subreddit information and hot
posts. Every request sends a custom User-Agent and avoids following redirects
so invalid subreddit names can be handled correctly.

## Files

- `0-subs.py` exposes `number_of_subscribers(subreddit)` and returns a
  subreddit's total subscriber count.
- `1-top_ten.py` exposes `top_ten(subreddit)` and prints the first ten hot-post
  titles.
- `2-recurse.py` exposes `recurse(subreddit)` and recursively returns every
  hot-post title.
- `3-count.py` exposes `count_words(subreddit, word_list)` and recursively
  prints sorted keyword counts from hot-post titles.

## Requirements

- Python 3
- `requests`

The functions use Reddit's public JSON endpoints under
`https://www.reddit.com/r/<subreddit>/`.
