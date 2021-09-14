#!/usr/bin/python3
""" extend past Python script to export data in the CSV format."""
from sys import argv
import json
import requests


if __name__ == '__main__':
    ID = argv[1]
    url = "https://jsonplaceholder.typicode.com/todos/?userId={}".format(ID)
    todoList = requests.get(url)
    url = "https://jsonplaceholder.typicode.com/users?id={}".format(ID)
    user = requests.get(url)
    tL = todoList.json()
    u = user.json()[0]
    name = u.get('username')
    file = "{}.json".format(ID)
    taskList = []
    for task in tL:
        jsonDict = {}
        jsonDict['title'] = task.get('title')
        jsonDict['completed'] = task.get('completed')
        jsonDict['username'] = name
        taskList.append(jsonDict)
    rDict = {}
    rDict[ID] = taskList
    with open(file, 'w') as f:
        json.dump(rDict, f)
