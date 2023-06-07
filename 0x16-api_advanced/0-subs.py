#!/usr/bin/python3
"""A function that queries the Reddit API and
returns the number of subscribers"""
import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}  # Set a custom User-Agent to avoid errors

    try:
        response = requests.get(url, headers=headers, timeout=5)  # Set a timeout of 5 seconds
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes

        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    except (requests.RequestException, KeyError):
        return 0

