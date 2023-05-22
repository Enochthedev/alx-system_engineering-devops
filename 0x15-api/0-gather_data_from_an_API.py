#!/usr/bin/python3
import requests
import sys

def get_employee_todo_progress(employee_id):
    # Fetch employee data from the API
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos/{employee_id}")
    
    if response.status_code == 200:
        employee_data = response.json()
        
        # Get the employee's name
        employee_name = employee_data['name']
        
        # Get the total number of tasks
        total_tasks = len(employee_data['todos'])
        
        # Get the number of completed tasks and their titles
        completed_tasks = [task['title'] for task in employee_data['todos'] if task['completed']]
        num_completed_tasks = len(completed_tasks)
        
        # Print the progress information
        print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_tasks}):")
        for task_title in completed_tasks:
            print("\t", task_title)
    else:
        print(f"Failed to retrieve employee data. Error: {response.status_code}")

if __name__ == '__main__':
    # Check if an employee ID is provided as a command-line argument
    if len(sys.argv) == 2:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    else:
        print("Please provide the employee ID as a command-line argument.")
