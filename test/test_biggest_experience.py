import unittest
from  src.find_the_biggest_experience import max_experience
import unittest

class TestMaxExperience(unittest.TestCase):
    def test_small_example(self):
        levels = 2
        experience = [
            [2],
            [2, 3]
        ]
        self.assertEqual(max_experience(levels, experience), 7)

    def test_max_path(self):
        levels = 4
        experience = [
            [7],
            [7, 8],
            [9, 1, 2],
            [3, 0, 0, 5]
        ]
        self.assertEqual(max_experience(levels, experience), 42)

if __name__ == '__main__':
    unittest.main()
