import json
from pathlib import Path
import unittest


class SettingsTest(unittest.TestCase):
    def test_limit(self):
        settings = json.loads((Path(__file__).resolve().parents[1] / "settings.json").read_text())
        self.assertIs(type(settings["limit"]), int)
        self.assertGreaterEqual(settings["limit"], 1)
