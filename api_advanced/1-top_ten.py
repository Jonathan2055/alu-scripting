#!/usr/bin/python3
"""
A function that queries the Reddit API and prints the titles.
"""

import requests


def top_ten(subreddit):
    """Prints the top ten hot posts for a given subreddit"""

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'alu-scripting:v1.0 (by /u/your_username)'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code != 200:
            return  # Do NOT print None, just return silently

        data = response.json().get("data", {})
        children = data.get("children", [])

        if not children:
            return  # Again, return silently if empty

        for post in children:
            print(post.get("data", {}).get("title"))

    except requests.RequestException:
        return
