#7

import unittest
from src.searck_of_morris_prat import kmp_search

class TestKMPSearch(unittest.TestCase):
    def test_single_match(self):
        text = "Hello, world!"
        pattern = "world"
        self.assertEqual(kmp_search(text, pattern), [7])

    def test_multiple_matches(self):
        text = "ababcababcab"
        pattern = "ab"
        self.assertEqual(kmp_search(text, pattern), [0, 2, 5, 7, 10])

    def test_no_match(self):
        text = "Python is awesome"
        pattern = "Java"
        self.assertEqual(kmp_search(text, pattern), [])

    def test_empty_text(self):
        text = ""
        pattern = "pattern"
        self.assertEqual(kmp_search(text, pattern), [])

if __name__ == "__main__":
    unittest.main()
