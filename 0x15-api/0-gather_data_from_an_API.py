#!/usr/bin/python3
"""Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress."""
import requests
from sys import argv


if __name__ == '__main__':
    ID = argv[1]
    url = "https://jsonplaceholder.typicode.com/todos/?userId={}".format(ID)
    todoList = requests.get(url)
    url = "https://jsonplaceholder.typicode.com/users?id={}".format(ID)
    user = requests.get(url)
    tL = todoList.json()
    u = user.json()[0]
    name = u.get('name')
    taskComplete = 0
    for tC in tL:
        taskComplete += 1 if tC.get('completed') else 0
    string = "Employee {} is done with tasks({}/20)"\
              .format(name, taskComplete)
    print(string)
    for task in tL:
        if task.get('completed'):
            print("\t {}".format(task.get('title')))
