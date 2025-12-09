import unittest
from todo_app import TodoApp

class TestTodoApp(unittest.TestCase):
    def setUp(self):
        """Set up a fresh TodoApp instance for each test."""
        self.app = TodoApp()

    def test_add_task(self):
        """Test adding a task."""
        self.app.add_task("Test Task", "Test Description")
        self.assertEqual(len(self.app.tasks), 1)
        self.assertEqual(self.app.tasks[0]['title'], "Test Task")
        self.assertEqual(self.app.tasks[0]['description'], "Test Description")
        self.assertEqual(self.app.tasks[0]['status'], "Incomplete")
        self.assertEqual(self.app.tasks[0]['id'], 1)

    def test_add_task_without_description(self):
        """Test adding a task without description."""
        self.app.add_task("Test Task")
        self.assertEqual(len(self.app.tasks), 1)
        self.assertEqual(self.app.tasks[0]['title'], "Test Task")
        self.assertEqual(self.app.tasks[0]['description'], "")

    def test_view_tasks_empty(self):
        """Test viewing tasks when the list is empty."""
        # This test ensures no error occurs when viewing empty list
        self.app.view_tasks()
        self.assertEqual(len(self.app.tasks), 0)

    def test_update_task(self):
        """Test updating a task's title and description."""
        self.app.add_task("Original Title", "Original Description")
        task_id = self.app.tasks[0]['id']
        
        # Update both title and description
        result = self.app.update_task(task_id, "New Title", "New Description")
        self.assertTrue(result)
        self.assertEqual(self.app.tasks[0]['title'], "New Title")
        self.assertEqual(self.app.tasks[0]['description'], "New Description")

    def test_update_task_partial(self):
        """Test updating only title or description."""
        self.app.add_task("Original Title", "Original Description")
        task_id = self.app.tasks[0]['id']
        
        # Update only title
        result = self.app.update_task(task_id, new_title="Updated Title")
        self.assertTrue(result)
        self.assertEqual(self.app.tasks[0]['title'], "Updated Title")
        self.assertEqual(self.app.tasks[0]['description'], "Original Description")

    def test_delete_task(self):
        """Test deleting a task."""
        self.app.add_task("Test Task")
        task_id = self.app.tasks[0]['id']
        
        result = self.app.delete_task(task_id)
        self.assertTrue(result)
        self.assertEqual(len(self.app.tasks), 0)

    def test_toggle_task_status(self):
        """Test toggling task status."""
        self.app.add_task("Test Task")
        task_id = self.app.tasks[0]['id']
        
        # Initially Incomplete
        self.assertEqual(self.app.tasks[0]['status'], "Incomplete")
        
        # Toggle to Complete
        result = self.app.toggle_task_status(task_id)
        self.assertTrue(result)
        self.assertEqual(self.app.tasks[0]['status'], "Complete")
        
        # Toggle back to Incomplete
        result = self.app.toggle_task_status(task_id)
        self.assertTrue(result)
        self.assertEqual(self.app.tasks[0]['status'], "Incomplete")

    def test_invalid_task_operations(self):
        """Test operations on non-existent tasks."""
        # Try updating a non-existent task
        result = self.app.update_task(999, "New Title")
        self.assertFalse(result)
        
        # Try deleting a non-existent task
        result = self.app.delete_task(999)
        self.assertFalse(result)
        
        # Try toggling status of a non-existent task
        result = self.app.toggle_task_status(999)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()