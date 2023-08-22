#!/usr/bin/python3
"""Convert JSON to CSV format"""
import requests
import sys
import json
import csv


if __name__ == "__main__":
    if len(sys.argv) == 2:
        id = sys.argv[1]
        user = "https://jsonplaceholder.typicode.com/users/{}".format(id)
        todos = "https://jsonplaceholder.typicode.com/todos?userId={}"\
                .format(id)

        username = requests.get(user).json().get("username")
        all_todos = requests.get(todos).json()

        with open(f"{id}.csv", 'w') as csv_file:
            f = csv.writer(csv_file, delimiter=",", quoting=csv.QUOTE_ALL)
            for todo in all_todos:
                f.writerow([sys.argv[1],
                           username,
                           todo["completed"],
                           todo["title"]])
