import unittest
from discount import discounted_subtotal


class DiscountTests(unittest.TestCase):
    def test_eligible(self):
        self.assertEqual(discounted_subtotal(120, 5, 15), 105)
