#5

import unittest
from src.check_for_cycle_in_graph import has_cycle

class TestCycleDetection(unittest.TestCase):
    def test_cycle(self):
        graph_cycle = {
            1: [2, 3],
            2: [1, 3, 5],
            3: [1, 2, 4],
            4: [3, 5],
            5: [2, 4, 1]  # introducing a cycle
        }
        self.assertTrue(has_cycle(graph_cycle))

    def test_empty_graph(self):
        graph_empty = {}
        self.assertFalse(has_cycle(graph_empty))

if __name__ == '__main__':
    unittest.main()
