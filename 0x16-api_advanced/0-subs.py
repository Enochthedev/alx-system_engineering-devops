#!/usr/bin/python3
"""A function that queries the Reddit API and
returns the number of subscribers"""
import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}  # Set a custom User-Agent to avoid errors

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            subscribers = data["data"]["subscribers"]
            return subscribers
        except KeyError:
            return 0
    else:
        return 0
