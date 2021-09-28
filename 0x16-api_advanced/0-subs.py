#!/usr/bin/python3
"""function that queries the Reddit API and returns the number of subscribers
If an invalid subreddit is given, the function should return 0"""
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """function that queries the Reddit API and returns the number of
    subscribers. If an invalid subreddit is given,
    the function should return 0"""
    subreddit = argv[1]
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers={'User-agent': 'MyScript'})
    data = response.json()
    subscribers = data.get('data').get('subscribers')
    return subscribers if subscribers else 0
