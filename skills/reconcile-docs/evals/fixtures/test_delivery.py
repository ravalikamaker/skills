"""Executable expectations derived from the accepted synthetic contract."""
import unittest
from delivery import deliver


class DeliveryContractTests(unittest.TestCase):
    def test_nonpositive_limit_rejects_before_sending(self):
        for attempts in (0, -2):
            with self.subTest(attempts=attempts):
                calls = []
                with self.assertRaises(ValueError):
                    deliver(lambda: calls.append("sent") or True, attempts)
                self.assertEqual(calls, [])

    def test_default_exhaustion_makes_three_calls(self):
        calls = []
        self.assertFalse(deliver(lambda: calls.append("sent") or False))
        self.assertEqual(len(calls), 3)

    def test_success_stops_before_limit(self):
        results = iter([False, True])
        calls = []
        self.assertTrue(deliver(lambda: calls.append("sent") or next(results), 5))
        self.assertEqual(len(calls), 2)


if __name__ == "__main__":
    unittest.main()
