#!/usr/bin/python3
"""
A function that queries the Reddit API and prints the top 10 hot posts of a subreddit
"""
import requests


def top_ten(subreddit):
    """ Prints the titles of the first 10 hot posts listed in a subreddit """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return  # ✅ Do not print anything

        posts = response.json().get('data', {}).get('children', [])
        for post in posts:
            print(post.get('data', {}).get('title'))

    except Exception:
        return  # ✅ Silently fail on errors
