#!/usr/bin/python3
"""Gather data from an API"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:
        id = sys.argv[1]
        user = "https://jsonplaceholder.typicode.com/users/{}".format(id)
        todos = "https://jsonplaceholder.typicode.com/todos?userId={}".format(id)

        name = requests.get(user).json().get("name")
        all_todos = requests.get(todos).json()
#       print(all_todos)
        completed_titles = []
        for todo in all_todos:
            if todo['completed'] is True:
                completed_titles.append(todo.get("title"))

        print("Employee {} is done with tasks({}/{}):".format(name,
            len(completed_titles), len(all_todos)))
        for completed_title in completed_titles:
            print('\t' + completed_title)

