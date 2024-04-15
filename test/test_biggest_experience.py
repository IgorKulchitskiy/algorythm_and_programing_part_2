##6
import unittest
from src.find_the_biggest_experience import max_experience

class TestMaxExperience(unittest.TestCase):

    def test_max_experience_first_level(self):
        levels = 1
        experience = [[9999]]
        self.assertEqual(max_experience(levels, experience), 9999)

    def test_max_experience_second_level(self):
        levels = 2
        experience = [[1], [8, 6]]
        self.assertEqual(max_experience(levels, experience), 13)


if __name__ == '__main__':
    unittest.main()
