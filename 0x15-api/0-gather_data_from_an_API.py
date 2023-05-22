#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""

import requests
import sys


def get_user_info(employee_id):
    """Returns the user information for the given employee ID."""
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Could not get user information for employee ID {}".format(employee_id))


def get_todo_list(employee_id):
    """Returns the to-do list for the given employee ID."""
    url = "https://jsonplaceholder.typicode.com/todos"
    params = {"userId": employee_id}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Could not get to-do list for employee ID {}".format(employee_id))


def get_completed_tasks(todo_list):
    """Returns a list of completed tasks from the given to-do list."""
    completed_tasks = []
    for task in todo_list:
        if task["completed"]:
            completed_tasks.append(task)
    return completed_tasks


def main():
    """The main function."""
    employee_id = sys.argv[1]
    user_info = get_user_info(employee_id)
    todo_list = get_todo_list(employee_id)
    completed_tasks = get_completed_tasks(todo_list)

    print("Employee {} is done with tasks({}/{}):".format(
        user_info["name"], len(completed_tasks), len(todo_list)))
    for task in completed_tasks:
        print("\t {}".format(task["title"]))


if __name__ == "__main__":
    main()
