#!/usr/bin/python3

"""Prints the titles of the top 10 hot posts of a subreddit"""
import requests

def top_ten(subreddit):
    url = "https://www.reddit.com/r/"+subreddit+"/hot.json?limit=10"
    headers = {"User-Agent": "alu-scripting:v1.0 (by /u/your_username)"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get("data", {}).get("children", [])
            for post in data:
                print(post.get("data", {}).get("title"))
        else:
            print(None)
    except requests.RequestException:
        print(None)
