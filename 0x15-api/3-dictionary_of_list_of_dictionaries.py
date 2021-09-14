#!/usr/bin/python3
""" extend past Python script to export data in the CSV format."""
import json
import requests


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/todos/"
    urlUser = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(urlUser)
    u = users.json()
    file = "todo_all_employees.json"
    with open(file, 'w') as f:
        rDict = {}
        for user in u:
            userDict = {}
            taskList= []
            todoList = requests.get(url)
            tL = todoList.json()
            name = user.get('username')
            for task in tL:
                jsonDict = {}
                jsonDict['username'] = name
                jsonDict['task'] = task.get('title')
                jsonDict['completed'] = task.get('completed')
                taskList.append(jsonDict)
        rDict[user.get('id')] = taskList
        json.dump(rDict, f)
