Task Tracker CLI

A lightweight, dependency-free command-line interface (CLI) task management utility written in Python.
It provides standard terminal commands to create, update, track, and delete tasks with local JSON file persistence.

Features

Zero External Dependencies: Built entirely using Python's standard library modules (sys, json, os, datetime).
Data Persistence: Automatically creates and updates a local tasks.json file in the working directory.
Status Lifecycle: Supports todo, in-progress, and done task states.
Timestamp Tracking: Automatically tracks createdAt and updatedAt timestamps for all operations.
Filtered Viewing: Allows listing all tasks or filtering the table display by status.

Requirements

Python 3.x  
Quick Start
Save the code into a file named task_tracker.py.
Open your terminal or command prompt in that directory.
Run commands using python task_tracker.py <command> [args].

Usage & Commands

Add a new task:- [python task_tracker.py add "Task description"]
List all tasks:- [python task_tracker.py list]
Filter tasks by status (todo, in-progress, done):- [python task_tracker.py list todo], [python task_tracker.py list in-progress], [python task_tracker.py list done]
Mark a task as in-progress:- [python task_tracker.py mark-in-progress 1]
Mark a task as done:- [python task_tracker.py mark-done 1]
Update task description:- [python task_tracker.py update 1 "Updated description"]
Delete a task:- [python task_tracker.py delete 1]

Storage Format (tasks.json)

Tasks are saved in JSON format using auto-incrementing unique IDs and ISO timestamps:

[
  {
    "id": 1,
    "description": "Breakfast",
    "status": "done",
    "createdAt": "2026-04-29T10:15:30.654321",
    "updatedAt": "2026-04-29T10:20:00.123456"
  }
]
```[cite: 1]

## Project Credits

* **Developer**: Fazil Ibni Mushtaq[cite: 1]
* **Supervisor**: Mr. Uvesh Ahmad[cite: 1]
* **Institution**: Centre for Innovation and Entrepreneurship, Jamia Millia Islamia[cite: 1]
