#!/usr/bin/python3
"""Gets data from an API and exports it to a JSON file.
"""
import json
import requests


API_URL = 'https://jsonplaceholder.typicode.com'
'''The APIs URL.'''


if __name__ == '__main__':
    users_res = requests.get('{}/users'.format(API_URL)).json()
    todos_res = requests.get('{}/todos'.format(API_URL)).json()
    users_data = {}
    for user in users_res:
        user_id = user.get('id')
        user_name = user.get('username')
        todos = list(filter(lambda x: x.get('userId') == user_id, todos_res))
        user_data = list(map(
            lambda x: {
                'username': user_name,
                'task': x.get('title'),
                'completed': x.get('completed')
            },
            todos
        ))
        users_data['{}'.format(user_id)] = user_data
    with open('todo_all_employees.json', 'w') as file:
        json.dump(users_data, file)
