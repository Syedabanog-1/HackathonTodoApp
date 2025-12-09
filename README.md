# Todo Console Application

A command-line todo application that stores tasks in memory.

## Overview
This application allows users to manage their tasks through a console interface. All tasks are stored in memory and will be lost when the application exits.

## Features

1. **Add Task**: Add a new task with a title and optional description
2. **View Task List**: Display all tasks with ID, status, title, and description
3. **Update Task**: Modify the title or description of an existing task
4. **Delete Task**: Remove a task from the list
5. **Mark as Complete/Incomplete**: Toggle the status of a task between "Complete" and "Incomplete"

## Requirements

- Python 3.13 or higher

## How to Run

1. Navigate to the `src` directory:
```bash
cd src
```

2. Run the application:
```bash
python main.py
```

## Usage

The application runs in a loop until the user chooses to exit. Follow the on-screen prompts to interact with the application:

- Choose option 1 to add a new task
- Choose option 2 to view all tasks
- Choose option 3 to update an existing task
- Choose option 4 to delete a task
- Choose option 5 to toggle a task's completion status
- Choose option 6 to exit the application