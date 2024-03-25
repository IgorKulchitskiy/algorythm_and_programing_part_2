import unittest
from priority_queue_for_binary_tree import PriorityQueue

class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.priority_queue = PriorityQueue()
        self.priority_queue.add_task("Task 1", 3)
        self.priority_queue.add_task("Task 2", 1)
        self.priority_queue.add_task("Task 3", 2)

    def test_add_task(self):
        self.priority_queue.add_task("Task 4", 5)
        self.assertEqual(self.priority_queue.traverse(), [("Task 2", 1), ("Task 3", 2), ("Task 1", 3), ("Task 4", 5)])
        
    def test_traverse(self):
        self.assertEqual(self.priority_queue.traverse(), [("Task 2", 1), ("Task 3", 2), ("Task 1", 3)])

if __name__ == "__main__":
    unittest.main()
