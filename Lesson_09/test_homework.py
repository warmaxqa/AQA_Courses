import unittest

from Lesson_09.homeworks_function import has_more_than_10_unique_chars

# import lesson 6 , task 6.1
class TestUniqueChar(unittest.TestCase):
    def test_more_than_10_unique(self):
        self.assertTrue(has_more_than_10_unique_chars("abcdefghijklm"))

    def test_exactly_10_unique(self):
        self.assertFalse(has_more_than_10_unique_chars("abcdefghij"))

    def test_less_than_10_unique(self):
        self.assertFalse(has_more_than_10_unique_chars("aaaaaddbgepx"))

    def test_no_unique_chars(self):
        self.assertFalse(has_more_than_10_unique_chars("xxxxttrwv"))

    def test_empty_string(self):
        self.assertFalse(has_more_than_10_unique_chars(""))

    def test_all_same_chars(self):
        self.assertFalse(has_more_than_10_unique_chars("absa"))

    def test_special_chars(self):
        self.assertTrue(has_more_than_10_unique_chars("!@#$%^&*()_+{}|"))

    def test_numbers_and_letters(self):
        self.assertTrue(has_more_than_10_unique_chars("1234567890abcdefg"))

    def test_repeating_pattern(self):
        self.assertFalse(has_more_than_10_unique_chars("abcabcabc"))

    def test_upper_lower_chars(self):
        self.assertTrue(has_more_than_10_unique_chars("UuIiOoNnMmLlDd"))

if __name__ == "__main__":
    unittest.main()
