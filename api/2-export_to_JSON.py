#!/usr/bin/python3
"""Export to JSON format"""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        id = sys.argv[1]
        user = "https://jsonplaceholder.typicode.com/users/{}".format(id)
        todos = "https://jsonplaceholder.typicode.com/todos?userId={}"\
                .format(id)

        username = requests.get(user).json().get("username")
        all_todos = requests.get(todos).json()
#       print(all_todos)
        tasks = []

        with open(f"{id}.json", 'w') as json_file:
            for todo in all_todos:
                tasks.append({"task":
                              todo.get("title"),
                              "completed": todo.get("completed"),
                              "username": username})
            json_file.write(json.dumps({id: tasks}))
