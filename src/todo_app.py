class TodoApp:
    def __init__(self):
        """Initialize the Todo application with an empty task list."""
        self.tasks = []
        self.next_id = 1
        
    def add_task(self, title, description=""):
        """Add a new task with a unique ID and default status 'Incomplete'."""
        task = {
            'id': self.next_id,
            'title': title,
            'description': description,
            'status': 'Incomplete'
        }
        self.tasks.append(task)
        self.next_id += 1
        print(f"Task added with ID {task['id']}: {title}")
        
    def view_tasks(self):
        """Display all tasks in a readable list format."""
        if not self.tasks:
            print("\nNo tasks found.")
            return
            
        print("\n" + "="*60)
        print("TASK LIST")
        print("="*60)
        
        for task in self.tasks:
            status_symbol = "[x]" if task['status'] == 'Complete' else "[ ]"
            print(f"ID: {task['id']:3} | {status_symbol} | {task['title']}")
            if task['description']:
                print(f"         Description: {task['description']}")
            print("-" * 60)
            
    def update_task(self, task_id, new_title=None, new_description=None):
        """Update the title or description of a task by its ID."""
        for task in self.tasks:
            if task['id'] == task_id:
                if new_title is not None:
                    task['title'] = new_title
                if new_description is not None:
                    task['description'] = new_description
                print(f"Task {task_id} updated successfully.")
                return True
        print(f"Task with ID {task_id} not found.")
        return False
        
    def delete_task(self, task_id):
        """Remove a task by its ID."""
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                deleted_task = self.tasks.pop(i)
                print(f"Task '{deleted_task['title']}' deleted successfully.")
                return True
        print(f"Task with ID {task_id} not found.")
        return False
    
    def toggle_task_status(self, task_id):
        """Toggle the status of a task between 'Complete' and 'Incomplete'."""
        for task in self.tasks:
            if task['id'] == task_id:
                task['status'] = 'Complete' if task['status'] == 'Incomplete' else 'Incomplete'
                status = task['status']
                print(f"Task {task_id} marked as {status}.")
                return True
        print(f"Task with ID {task_id} not found.")
        return False
        
    def get_user_choice(self):
        """Display menu options and get user choice."""
        print("\n" + "="*40)
        print("TODO CONSOLE APPLICATION")
        print("="*40)
        print("1. Add Task")
        print("2. View Task List")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark as Complete/Incomplete")
        print("6. Exit")
        print("-"*40)
        
        try:
            choice = int(input("Enter your choice (1-6): "))
            return choice
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
            return None
    
    def run(self):
        """Main application loop."""
        print("Welcome to the Todo Console Application!")
        
        while True:
            choice = self.get_user_choice()
            
            if choice == 1:
                # Add Task
                title = input("Enter task title: ").strip()
                if not title:
                    print("Task title cannot be empty.")
                    continue
                description = input("Enter task description (optional): ").strip()
                self.add_task(title, description)
                
            elif choice == 2:
                # View Task List
                self.view_tasks()
                
            elif choice == 3:
                # Update Task
                self.view_tasks()
                if not self.tasks:
                    continue
                    
                try:
                    task_id = int(input("Enter task ID to update: "))
                    print("\nLeave blank to keep current value.")
                    new_title = input(f"Enter new title (current: {next((t['title'] for t in self.tasks if t['id'] == task_id), '')}): ").strip()
                    new_description = input(f"Enter new description (current: {next((t['description'] for t in self.tasks if t['id'] == task_id), '')}): ").strip()
                    
                    # Only update fields if user entered new values
                    update_data = {}
                    if new_title:
                        update_data['title'] = new_title
                    if new_description:
                        update_data['description'] = new_description
                        
                    if update_data:
                        self.update_task(
                            task_id, 
                            new_title if new_title else None,
                            new_description if new_description else None
                        )
                    else:
                        print("No changes made.")
                        
                except ValueError:
                    print("Invalid task ID. Please enter a number.")
                    
            elif choice == 4:
                # Delete Task
                self.view_tasks()
                if not self.tasks:
                    continue
                    
                try:
                    task_id = int(input("Enter task ID to delete: "))
                    self.delete_task(task_id)
                except ValueError:
                    print("Invalid task ID. Please enter a number.")
                    
            elif choice == 5:
                # Mark as Complete/Incomplete
                self.view_tasks()
                if not self.tasks:
                    continue
                    
                try:
                    task_id = int(input("Enter task ID to toggle status: "))
                    self.toggle_task_status(task_id)
                except ValueError:
                    print("Invalid task ID. Please enter a number.")
                    
            elif choice == 6:
                # Exit
                print("Thank you for using the Todo Console Application!")
                break
                
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")