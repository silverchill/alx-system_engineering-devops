#!/usr/bin/python3

import requests
from sys import argv

if __name__ == "__main__":
    number = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(number)).json()
    todos = requests.get(url + "todos", params={"userId": number}).json()

    completed = [w.get("title") for w in todos if w.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(i)) for i in completed]