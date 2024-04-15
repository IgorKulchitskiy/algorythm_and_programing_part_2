#4_

import unittest
from src.priority_queue_for_binnary_tree import PriorityQueue

class TestPriority(unittest.TestCase):

    def test_add_task(self):
        priority_queue = PriorityQueue()
        priority_queue.add_task("Task 1", 3)
        priority_queue.add_task("Task 2", 1)
        priority_queue.add_task("Task 3", 2)
        
        expected_traversal = [("Task 2", 1), ("Task 3", 2), ("Task 1", 3)]
        self.assertEqual(priority_queue.traverse(), expected_traversal)

    def test_traverse_empty_queue(self):
        priority_queue = PriorityQueue()
        self.assertEqual(priority_queue.traverse(), [])

    def test_remove_from_empty_queue(self):
        priority_queue = PriorityQueue()
        removed_task = priority_queue.remove_highest_priority_task()
        self.assertIsNone(removed_task)

if __name__ == '__main__':
    unittest.main()
