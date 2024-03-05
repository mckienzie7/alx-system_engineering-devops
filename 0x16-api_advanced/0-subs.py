#!/usr/bin/python3
"""Get number of subscribers for a particular subreddit"""
import requests


def number_of_subscribers(subreddit):
    user_agent = 'Linux:Ubuntu/google'

    headers = {
        'User-Agent': user_agent
    }

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)
    try:
        my_dict = res.json()['data']
    except KeyError:
        return 0

    if not my_dict:
        return 0
    if res.status_code != 200:
        return 0
    if 'subscribers' not in my_dict.keys():
        return 0
    else:
        return my_dict['subscribers']
