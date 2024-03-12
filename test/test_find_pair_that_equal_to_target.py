#1
import unittest
from def_find_pair_with_sum import find_pair_which_equal_target

class Test(unittest.TestCase):
    def test_true(self):
        numbers = [ 2 , 7 , 11 , 15]
        target = 9 
        result = find_pair_which_equal_target(numbers , target)
        self.assertIsNotNone(result)
        self.assertEqual(result, (0, 1))


    def test_false(self):
        numbers = [3 , 5]
        target = 6
        result = find_pair_which_equal_target(numbers , target)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()