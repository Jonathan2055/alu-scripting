#!/usr/bin/python3



"""Recursively gets all hot post titles from a subreddit"""
import requests

def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "alu-scripting:v1.0 (by /u/your_username)"}
    params = {"after": after}
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            return None
        data = response.json().get("data", {})
        posts = data.get("children", [])
        for post in posts:
            hot_list.append(post.get("data", {}).get("title"))
        after = data.get("after")
        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list
    except requests.RequestException:
        return None
