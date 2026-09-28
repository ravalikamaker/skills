import unittest
from api import amount_for_legacy


class LegacyContractTests(unittest.TestCase):
    def test_legacy_amounts(self):
        for cents, text in ((123, "1.23"), (0, "0.00"), (-123, "-1.23")):
            with self.subTest(cents=cents):
                self.assertEqual(amount_for_legacy(cents), text)
