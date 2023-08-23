#!/usr/bin/python3
"""Export to JSON format"""
import json
import requests


if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(users_url).json()
#   print(users)

    all_tasks = {}
    for user in users:
        user_id = user.get("id")
        user_name = user.get("username")
        todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}"\
                    .format(user_id)
        todos = requests.get(todos_url).json()
        tasks = []
        for todo in todos:
            task = {"username": user_name,
                    "task": todo.get("title"),
                    "completed": todo.get("completed")}
            tasks.append(task)
        all_tasks[user_id] = tasks

    with open("todo_all_employees.json", "w") as json_file:
        json_file.write(json.dumps(all_tasks))
