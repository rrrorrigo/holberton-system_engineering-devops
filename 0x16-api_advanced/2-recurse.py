#!/usr/bin/python3
"""recursive function that queries the Reddit API"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    '''Request subs number of given subreddit'''
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'\
          .format(subreddit, after)
    req = requests.get(url, headers={'User-agent': 'MyScript'},
                       allow_redirects=False)
    if req.status_code != 200:
        return None
    r = req.json()
    for title in r.get('data').get('children'):
        hot_list.append(title.get('data').get('title'))
    afterId = r.get('data').get('after')
    if afterId is not None:
        recurse(subreddit, hot_list, afterId)
    return hot_list
