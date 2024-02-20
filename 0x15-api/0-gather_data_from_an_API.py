#!/usr/bin/python3
"""This module contains a script to gather data from an API
"""
import re
import requests
import sys


API_URL = 'https://jsonplaceholder.typicode.com'
'''The APIs URL.'''


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            user_id = int(sys.argv[1])
            user_res = requests.get('{}/users/{}'.format(API_URL, user_id)).json()
            todos_res = requests.get('{}/todos'.format(API_URL)).json()
            user_name = user_res.get('name')
            todos = list(filter(lambda x: x.get('userId') == user_id, todos_res))
            todos_done = list(filter(lambda x: x.get('completed'), todos))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    user_name,
                    len(todos_done),
                    len(todos)
                )
            )
            for todo_done in todos_done:
                print('\t {}'.format(todo_done.get('title')))