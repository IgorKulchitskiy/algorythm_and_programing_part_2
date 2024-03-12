import unittest
from main import sorting

class TestSortAndMergeIntervals(unittest.TestCase):
    def test_sort_and_merge_intervals(self):
        tuple_list = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
        merged_intervals = sorting(tuple_list)
        self.assertEqual(merged_intervals, [(0, 1), (3, 8), (9, 12)])

    def test_sort_and_merge_intervals_single_interval(self):
        tuple_list = [(1, 2)]
        merged_intervals = sorting(tuple_list)
        self.assertEqual(merged_intervals, [(1, 2)])

    def test_sort_and_merge_intervals_all_overlapping_intervals(self):
        tuple_list = [(1, 3), (2, 4), (3, 5)]
        merged_intervals = sorting(tuple_list)
        self.assertEqual(merged_intervals, [(1, 5)])

    def test_sort_and_merge_intervals_single_interval(self):
        tuples = [(0, 7),(5, 6)]
        merged_intervals = sorting(tuples)
        self.assertEqual(merged_intervals, [(0, 7)])

if __name__ == '__main__':
    unittest.main()
