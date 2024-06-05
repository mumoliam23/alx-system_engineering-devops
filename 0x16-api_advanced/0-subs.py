#!/usr/bin/python3
"""
Importing request module
"""
from requests import get

def number_of_subscribers(subreddit):
    """
    A function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit.
    """
    if not subreddit or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-Agent': 'Google Chrome Version 81.0.4044.129'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    try:
        response = get(url, headers=user_agent, allow_redirects=False)

        if response.status_code == 200:
            all_data = response.json()
            return all_data['data']['subscribers']
        else:
            return 0
    except Exception:
        return 0
