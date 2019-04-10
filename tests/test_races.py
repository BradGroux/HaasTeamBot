import maya
import unittest

from freezegun import freeze_time

from .context import haasbot
from haasbot.race import Race


@freeze_time("2019-03-03")
class RaceObjectTests(unittest.TestCase):
    """Basic race object and data functionality test cases."""

    def test_race_object_initializes_with_next_race_round(self):
        r = Race()
        self.assertEqual(r.round, "1")

    def test_race_object_initializes_with_next_race_name(self):
        r = Race()
        self.assertEqual(r.name, "Australian Grand Prix")

    def test_race_object_initializes_with_correct_datetime(self):
        r = Race()
        expected_datetime = maya.parse("2019-03-17 05:10:00Z")
        self.assertEqual(r.race_datetime, expected_datetime)

    def test_race_object_correct_weekend_range(self):
        r = Race()
        expected_weekend_range_string = "Fri 15 Mar - Sun 17 Mar"
        actual_weekend_range_string = r.race_weekend_range()
        self.assertEqual(actual_weekend_range_string, expected_weekend_range_string)


if __name__ == "__main__":
    unittest.main()
