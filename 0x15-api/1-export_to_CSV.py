#!/usr/bin/python3
"""export data in the CSV format"""

import csv
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

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
           [user_id, username_list, t.get("completed"), t.get("title")]
        ) for t in todo_list]
