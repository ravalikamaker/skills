import unittest
from labels import add_label, preview_label


class LabelTests(unittest.TestCase):
    def test_shared_rule_and_effect(self):
        events = []
        self.assertEqual(add_label("  Urgent ", events), "urgent")
        self.assertEqual(preview_label(" URGENT "), "urgent")
        self.assertEqual(events, ["urgent"])

    def test_rejection_has_no_effect(self):
        for value, error, message in [("  ", ValueError, "label must not be blank"),
                                      (None, TypeError, "label must be text")]:
            with self.subTest(value=value):
                events = []
                with self.assertRaisesRegex(error, message):
                    add_label(value, events)
                with self.assertRaisesRegex(error, message):
                    preview_label(value)
                self.assertEqual(events, [])
