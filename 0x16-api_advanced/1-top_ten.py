#!/usr/bin/python3
"""Get number of subscribers for a particular subreddit"""
import requests


def top_ten(subreddit):
    user_agent = 'Linux:Ubuntu/google'

    headers = {
        'User-Agent': user_agent
    }
    params = {
        'limit': 10
    }
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    res = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
            )

    if res.status_code == 200:
        try:
            hot_posts = res.json()['data']['children']
            for post in hot_posts:
                print(post['data']['title'])
        except KeyError:
            print("None")
    else:
        print("None")
