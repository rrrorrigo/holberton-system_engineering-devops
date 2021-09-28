#!/usr/bin/python3
"""function that queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(url, headers={'User-agent': 'MyScript'},
                            allow_redirects=False)
    if response.status_code != 200:
        print("None")
        return
    data = response.json()
    hotpost = data.get('data').get('children')
    for i in range(10):
        print(hotpost[i].get('data').get('title'))
