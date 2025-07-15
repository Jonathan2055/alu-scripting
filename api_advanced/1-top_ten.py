#!/usr/bin/python3
"""Importing request modula"""
import requests


def top_ten(subreddit):
    """Prints the first 10 hot post titles of a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "alu-scripting:v1.0 (by /u/your_username)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print("None")
            return

        data = response.json().get("data", {}).get("children", [])
        for post in data:
            print(post.get("data", {}).get("title"))

    except Exception:
        print("None")
