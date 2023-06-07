#!/usr/bin/python3
""" Module for storing the count_words function. """
import requests

def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively queries the Reddit API, parses the titles of all hot articles for a given subreddit,
    and prints a sorted count of given keywords.

    Args:
        subreddit (str): The subreddit to query.
        word_list (list): A list of keywords to count.
        after (str, optional): A pagination token to retrieve the next page of results. Defaults to None.
        counts (dict, optional): A dictionary to store the keyword counts. Defaults to None.

    Returns:
        None
    """
    if counts is None:
        counts = {}

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
            title = post["data"]["title"].lower()
            words = title.split()

            for word in word_list:
                word_lower = word.lower()
                count = words.count(word_lower)
                if count > 0:
                    counts[word_lower] = counts.get(word_lower, 0) + count

        if after:
            return count_words(subreddit, word_list, after=after, counts=counts)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    except (requests.RequestException, KeyError):
        return
