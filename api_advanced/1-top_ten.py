#!/usr/bin/python3
"""
A function that queries the Reddit API and prints the top 10 hot posts of a subreddit
"""
import requests


def top_ten(subreddit):
    """Print the titles of the top 10 hot posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        'User-Agent': 'alu-api-advanced:top_ten:v1.0 (by /u/alu_student)'
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return

        data = response.json().get("data", {}).get("children", [])
        if not data:
            return

        for post in data:
            print(post.get("data", {}).get("title"))

    except Exception:
        return
