#5

import unittest

class TestCycleDetection(unittest.TestCase):
    def test_no_cycle(self):
        graph_no_cycle = {
            1: [2, 3],
            2: [1, 3, 5],
            3: [1, 2, 4],
            4: [3, 5],
            5: [2, 4]
        }
        self.assertFalse(has_cycle(graph_no_cycle))

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
