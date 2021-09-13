#!/usr/bin/python3
""" extend past Python script to export data in the CSV format."""
import requests
import csv
from sys import argv

from requests import models


if __name__ == '__main__':
    ID = argv[1]
    url = "https://jsonplaceholder.typicode.com/todos/?userId={}".format(ID)
    todoList = requests.get(url)
    url = "https://jsonplaceholder.typicode.com/users?id={}".format(ID)
    user = requests.get(url)
    tL = todoList.json()
    u = user.json()[0]
    name = u.get('username')
    file = "{}.csv".format(ID)
    with open(file, mode='w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for task in tL:
            status = task.get('completed')
            title = task.get('title')
            writer.writerow([ID, name, status, title])
