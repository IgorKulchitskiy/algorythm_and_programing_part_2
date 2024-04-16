import unittest
from src.find_the_biggest_experience import maximum_experience

class TestMaxExperience(unittest.TestCase):
    def test_small_example(self):
        levels = 2
        experience = [
            [2],
            [2, 3]
        ]
        self.assertEqual(maximum_experience(levels, experience), 5)

    def test_max_path(self):
        levels = 4
        experience = [
            [7],
            [7, 8],
            [2, 1, 9],
            [3, 0, 0, 5]
        ]
        self.assertEqual(maximum_experience(levels, experience), 29)

    def test_high_value(self):
        levels = 1
        experience = [
            [9999]
        ]
        self.assertEqual(maximum_experience(levels, experience), 9999)

if __name__ == '__main__':
    unittest.main()
