# Phase I: Todo Console App Specification

## Overview
Build a command-line todo application that stores tasks in memory.

## Functional Requirements
The app must implement the following 5 features:

1. **Add Task**: 
   - User can input a task title and an optional description.
   - System assigns a unique ID.
   - Default status is "Incomplete".

2. **View Task List**: 
   - Display all tasks in a readable list format.
   - Show ID, Title, Status ( [ ] or [x] ), and Description.

3. **Update Task**: 
   - User selects a task by ID.
   - User can modify the Title or Description.

4. **Delete Task**: 
   - User selects a task by ID.
   - System removes it from the list.

5. **Mark as Complete**: 
   - User toggles the status of a task between "Complete" and "Incomplete".

## Technical constraints
- Use Python 3.13+.
- Use a `main.py` entry point.
- Ensure the application runs in a loop until the user chooses to "Exit".s