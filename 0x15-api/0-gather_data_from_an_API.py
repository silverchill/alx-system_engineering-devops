#!/usr/bin/python3

import requests
from sys import argv

if __name__ == "__main__":
    num_ = argv[1]
    given_url = "https://jsonplaceholder.typicode.com/"
    user_url = "{}/users/{}".format(given_url, num_)
    todo_url = "{}/todos?userId={}".format(given_url, num_)
    user = requests.get(user_url)
    todo = requests.get(todo_url)
    
    todo_list = todo.json()
    user_list = user.json()['name']
    ini_length = len(user_list)
    length = 0

    for task in todo_list:
        if task['completed'] is True:
            length += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(user_list, length, ini_length))
    for task in todo_list:
        if task['completed'] is True:
            print('\t {}'.format(task['title']))
