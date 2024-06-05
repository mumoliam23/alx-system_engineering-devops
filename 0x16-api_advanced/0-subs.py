#!/usr/bin/python3
"""
Importing request module
"""
from requests import get

def number_of_subscribers(subreddit):
    """
    A function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit.)
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    user_agent = {'User-Agent': 'Google Chrome Version 81.0.4044.129'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = get(url, headers=user_agent)
    all_data = response.json()

    try:
        return data['data']['subscribers']
    except:
        return 0
