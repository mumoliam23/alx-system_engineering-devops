#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If an invalid subreddit is given, returns 0.
    """
    # Define the headers to avoid rate limiting
    headers = {'User-Agent': 'custom user agent for querying subreddit subscribers'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    
    try:
        # Corrected typo: Use requests.get instead of response.get
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0
