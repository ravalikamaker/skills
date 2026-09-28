import unittest
from parse_count import parse_count


class ParseCountTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(parse_count(""), 0)

    def test_existing_nonempty(self):
        for text, number in (("0", 0), ("12", 12), ("-3", -3)):
            with self.subTest(text=text):
                self.assertEqual(parse_count(text), number)
