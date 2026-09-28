import unittest
from helpers import total_for_pair, total_with_fee


class HelperTests(unittest.TestCase):
    def test_public_callers(self):
        self.assertEqual(total_for_pair(3), 6)
        self.assertEqual(total_for_pair(0), 0)
        self.assertEqual(total_with_fee(3, 2), 8)
        self.assertEqual(total_with_fee(-2, 1), -3)
