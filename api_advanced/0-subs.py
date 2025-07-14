#!/usr/bin/python3
"""Gets number of subscribers for a given subreddit"""
import requests

def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/"+subreddit+"/about.json"
    headers = {"User-Agent": "alu-scripting:v1.0 (by /u/your_username)"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            return response.json().get("data", {}).get("subscribers", 0)
    except requests.RequestException:
        pass
    return 0
