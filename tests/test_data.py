import unittest

from freezegun import freeze_time

from .context import haasbot
import haasbot.data as d


@freeze_time("2019-03-03")
class DataFunctionTests(unittest.TestCase):
    """Basic data functionality test cases."""

    def test_get_next_race(self):
        next_race = d.get_next_race()
        expected_race_name = "Australian Grand Prix"
        self.assertEqual(expected_race_name, next_race["raceName"])


if __name__ == "__main__":
    unittest.main()
