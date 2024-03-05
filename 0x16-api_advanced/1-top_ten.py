#!/usr/bin/python3
"""
Contains a function to get top 10 hot posts from reddit
"""
import requests

BASE_URL = "https://www.reddit.com/r/"
"""Base url for reddit"""


def top_ten(subreddit):
    """GETs the top 10 hot posts from reddit API"""
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
    sort = 'top'
    limit = '10'
    result = requests.get(
        '{}/{}/.json?sort={}&limit={}'.format(
            BASE_URL, subreddit, sort, limit
        ),
        headers=header,
        allow_redirects=False
    )

    if result.status_code == 200:
        for post in result.json()['data']['children'][0:10]:
            print(post['data']['title'])
    else:
        print(None)
