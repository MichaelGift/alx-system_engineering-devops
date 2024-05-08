#!/usr/bin/python3
"""
Contains functions used to get number of active subreddit subscribers
"""
import requests

BASE_URL = """https://www.reddit.com"""
"""Reddit's base API url"""


def number_of_subscribers(subreddit):
    """GETs the number of subscribers in a given subreddit"""

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

    result = requests.get(
        '{}/r/{}/about.json'.format(BASE_URL, subreddit),
        headers=header,
        allow_redirects=False
    )

    if result.status_code == 200:
        return result.json()['data']['subscribers']
    return 0
