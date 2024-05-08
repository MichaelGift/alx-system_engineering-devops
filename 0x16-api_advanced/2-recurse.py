#!/usr/bin/python3
"""
Get top 10 hot posts from reddit
"""
import requests

BASE_URL = "https://www.reddit.com/r/"
"""Base url for reddit"""


def recurse(subreddit, hot_list=[], n=0, after=None):
    """Get the top 10 hot posts from reddit API"""
    header = {
        'Accept': 'application/json',
        'User-Agent': ' '.join([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'AppleWebkit/537.36 (KHTML, like Gecko)',
            'Chrome/97.0.4692.71',
            'Safari/537.36',
            'Edge/97.0.1072.62'
        ])
    }
    sort = 'hot'
    limit = 30
    result = requests.get(
        '{}/{}/.json?sort={}&limit={}&count={}&after={}'.format(
            BASE_URL, subreddit, sort, limit, n, after if after else ''),
        headers=header,
        allow_redirects=False
    )

    if result.status_code == 200:
        data = result.json()['data']
        posts = data['children']
        count = len(posts)
        hot_list.extend(list(map(lambda x: x['data']['title'], posts)))

        if count >= limit and data['after']:
            return recurse(subreddit, hot_list, n+count, data['after'])
        else:
            return hot_list if hot_list else None
    else:
        return hot_list if hot_list else None
