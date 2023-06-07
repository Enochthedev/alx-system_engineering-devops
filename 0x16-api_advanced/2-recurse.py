#!/usr/bin/python3
"""A recursive function that queries the Reddit
API and returns a list containing the titles of
all hot articles for a given subreddit."""
import requests

def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []
        
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {"User-Agent": "Mozilla/5.0"}  # Set a custom User-Agent to avoid errors
    params = {"after": after} if after else None

    try:
        response = requests.get(url, headers=headers, params=params, timeout=5)  # Set a timeout of 5 seconds
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes

        data = response.json()
        posts = data["data"]["children"]
        after = data["data"]["after"]
        
        for post in posts:
            title = post["data"]["title"]
            hot_list.append(title)

        if after:
            return recurse(subreddit, hot_list, after=after)
        else:
            return hot_list
    except (requests.RequestException, KeyError):
        return None
