#!/usr/bin/python3
"""function that queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers={'User-agent': 'MyScript'})
    data = response.json()
    data = data.get('data').get('children')
    if not data:
        print("None")
    for i in range(len(data)):
        if i < 10:
            print(data[i].get('data').get('title'))
