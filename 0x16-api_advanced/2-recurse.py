#!/usr/bin/python3
"""recursive function that queries the Reddit API"""
import requests


def recurse(subreddit, hot_list=[]):
    '''Request subs number of given subreddit'''
    url = 'https://www.reddit.com/r/{}.json'.format(subreddit)
    req = requests.get(url, headers={'User-agent': 'your bot 0.1'})
    r = req.json()['data']['children']
    hot_list = aux(hot_list, 0, r)
    afterId = req.json()['data']['after']
    while afterId is not None:
        afterId = req.json()['data']['after']
        url = 'https://www.reddit.com/r/{}.json?after={}'.format(subreddit, afterId)
        req = requests.get(url, headers={'User-agent': 'your bot 0.1'})
        r = req.json()['data']['children']
        hot_list += aux(hot_list, 0, r)
    return hot_list

def aux(hot_list, i, page_list):
    '''Request subs number of given subreddit'''
    if i == len(page_list):
        return hot_list
    else:
        hot_list.append(page_list[i]['data']['title'])
        i += 1
        return aux(hot_list, i, page_list)
