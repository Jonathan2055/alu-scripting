#!/usr/bin/pyhton3


"""Counts keyword occurrences in subreddit hot posts"""
import requests

def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}
        for word in word_list:
            counts[word.lower()] = 0

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "alu-scripting:v1.0 (by /u/your_username)"}
    params = {"after": after, "limit": 100}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            return

        data = response.json().get("data", {})
        posts = data.get("children", [])
        for post in posts:
            title = post.get("data", {}).get("title", "").lower().split()
            for word in title:
                for key in counts.keys():
                    if word == key:
                        counts[key] += 1

        after = data.get("after")
        if after:
            count_words(subreddit, word_list, after, counts)
        else:
            # Sort and print
            sorted_counts = sorted(
                [(k, v) for k, v in counts.items() if v > 0],
                key=lambda x: (-x[1], x[0])
            )
            for word, count in sorted_counts:
                print(f"{word}: {count}")

    except requests.RequestException:
        return
