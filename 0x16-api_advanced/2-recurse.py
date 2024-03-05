#!/usr/bin/python3
"""Hot articles on reddit"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    user_agent = 'Linux:Ubuntu/google'
    headers = {
        'User-Agent': user_agent
    }
    params = {
        'limit': 100,
        'after': after
    }
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
            )

    if response.status_code != 200:
        return None

    data = response.json().get('data', {})
    children = data.get('children', [])

    for child in children:
        hot_list.append(child['data']['title'])

    after = data.get('after')
    if after:
        return recurse(subreddit, hot_list, after=after)
    else:
        return hot_list
