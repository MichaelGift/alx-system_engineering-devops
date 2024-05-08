#!/usr/bin/python3
"""
Count occurrences of specific words in subreddit post titles.
"""
import requests


def sort_histogram(histogram={}):
    """
    Sort the histogram by word count and then alphabetically.
    Print the sorted histogram.
    """
    histogram = [(k, v) for k, v in histogram.items() if v]
    histogram_dict = {}
    for item in histogram:
        if item[0] in histogram_dict:
            histogram_dict[item[0]] += item[1]
        else:
            histogram_dict[item[0]] = item[1]
    histogram = list(histogram_dict.items())
    histogram.sort(key=lambda kv: kv[0], reverse=False)
    histogram.sort(key=lambda kv: kv[1], reverse=True)
    res_str = '\n'.join(['{}: {}'.format(kv[0], kv[1]) for kv in histogram])
    if res_str:
        print(res_str)


def count_words(subreddit, word_list, histogram=[], n=0, after=None):
    """
    Count occurrences of words in subreddit post titles.
    """
    api_headers = {
        'Accept': 'application/json',
        'User-Agent': ' '.join([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'AppleWebKit/537.36 (KHTML, like Gecko)',
            'Chrome/97.0.4692.71',
            'Safari/537.36',
            'Edge/97.0.1072.62'
        ])
    }
    sort = 'hot'
    limit = 30
    res = requests.get(
        '{}/r/{}/.json?sort={}&limit={}&count={}&after={}'.format(
            'https://www.reddit.com',
            subreddit,
            sort,
            limit,
            n,
            after if after else ''
        ),
        headers=api_headers,
        allow_redirects=False
    )
    if not histogram:
        word_list = [word.lower() for word in word_list]
        histogram = [(word, 0) for word in word_list]
    if res.status_code == 200:
        data = res.json()['data']
        posts = data['children']
        titles = [post['data']['title'] for post in posts]
        for word, count in histogram:
            for txt in titles:
                histogram[word] += txt.lower().split().count(word)
        if len(posts) >= limit and data['after']:
            count_words(
                subreddit,
                word_list,
                histogram,
                n + len(posts),
                data['after']
            )
        else:
            sort_histogram(histogram)
    else:
        return
