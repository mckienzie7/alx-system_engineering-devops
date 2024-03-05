#!/usr/bin/python3
"""My work """
import requests


def count_words(subreddit, word_list, instances={}, after=None, count=0):
    user_agent = 'Linux:Ubuntu/google'
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        'User-Agent': user_agent
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    response = requests.get(
            url, headers=headers,
            params=params, allow_redirects=False
            )

    try:
        results = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    results = results.get("data")
    after = results.get("after")
    count += results.get("dist")

    for c in results.get("children"):
        title = c.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                times = title.count(word.lower())
                instances[word] = instances.get(word, 0) + times

    if after is None:
        if not instances:
            print("")
        else:
            sorted_instances = sorted(
                    instances.items(),
                    key=lambda kv: (-kv[1], kv[0])
                    )
            [print(f"{k}: {v}") for k, v in sorted_instances]
    else:
        count_words(subreddit, word_list, instances, after, count)
