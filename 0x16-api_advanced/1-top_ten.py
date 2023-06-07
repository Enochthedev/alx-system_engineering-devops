#!/usr/bin/python3
"""A function that queries the Reddit API and
prints the titles of the first 10 hot posts
listed for a given subreddit."""
import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0"}  # Set a custom User-Agent to avoid errors

    try:
        response = requests.get(url, headers=headers, timeout=5)  # Set a timeout of 5 seconds
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes

        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            title = post["data"]["title"]
            print(title)
    except (requests.RequestException, KeyError):
        print("None")


