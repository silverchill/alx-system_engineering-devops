#!/usr/bin/python3
"""Exporting data in JSON format"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    given_url = "https://jsonplaceholder.typicode.com/"
    user_url = "{}/users/{}".format(given_url, user_id)
    todo_url = "{}/todos?userId={}".format(given_url, user_id)
    user = requests.get(user_url)
    todo = requests.get(todo_url)

    todo_list = todo.json()
    user_list = user.json()['name']
    username_list = user.json()['username']
    ini_length = len(todo.json())
    length = 0

    with open("{}.json".format(user_id), "w", newline="") as jsonfile:
        json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username_list
            } for t in todo_list]}, jsonfile)
