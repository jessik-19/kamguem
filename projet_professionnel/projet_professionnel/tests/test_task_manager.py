import unittest
from task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def test_add_task(self):
        manager = TaskManager()
        manager.add_task("Test Task")
        self.assertIn("Test Task", manager.tasks)

if __name__ == '__main__':
   unittest.main()
   