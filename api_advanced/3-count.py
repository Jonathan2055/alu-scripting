#!/usr/bin/python3
"""Recursive Reddit API keyword counter."""

import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """Counts keywords in subreddit hot posts recursively."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "alu-scripting:v1.0 (by /u/your_username)"}
    params = {"after": after}
    word_list = [word.lower() for word in word_list]

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)
        if response.status_code != 200:
            return

        data = response.json().get("data", {})
        posts = data.get("children", [])
        after = data.get("after")

        for post in posts:
            title = post.get("data", {}).get("title", "").lower().split()
            for word in title:
                if word in word_list:
                    word_count[word] = word_count.get(word, 0) + 1

        if after:
            return count_words(subreddit, word_list, after, word_count)

        # Sort and print
        for word, count in sorted(word_count.items(),
                                  key=lambda x: (-x[1], x[0])):
            if count > 0:
                print(f"{word}: {count}")

    except requests.RequestException:
        return
