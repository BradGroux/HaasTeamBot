import maya
import unittest

from freezegun import freeze_time

from .context import haasbot
from haasbot.race import Race


@freeze_time("2019-04-10")
class RaceObjectTests(unittest.TestCase):
    """Basic race object and data functionality test cases."""

    def setUp(self):
        self.r = Race()

    def test_race_object_initializes_with_next_race_round(self):
        self.assertEqual(self.r.round, "3")

    def test_race_object_initializes_with_next_race_name(self):
        self.assertEqual(self.r.name, "Chinese Grand Prix")

    def test_race_object_has_correct_location(self):
        self.assertEqual(self.r.location, "Shanghai")

    def test_race_object_has_correct_circuit_url(self):
        expected_circuit_url = (
            "https://en.wikipedia.org/wiki/Shanghai_International_Circuit"
        )
        self.assertEqual(self.r.circuit_url, expected_circuit_url)

    def test_race_object_initializes_with_correct_datetime(self):
        expected_datetime = maya.parse("2019-04-14 06:10:00Z")
        self.assertEqual(self.r.race_datetime, expected_datetime)

    def test_race_object_correct_weekend_range(self):
        expected_weekend_range_string = "Fri 12 Apr - Sun 14 Apr"
        actual_weekend_range_string = self.r.race_weekend_range()
        self.assertEqual(actual_weekend_range_string, expected_weekend_range_string)

    def test_race_object_timezone_list(self):
        expected_timezone_dict = {
            "utc": "14 Apr 06:10",
            "est": "14 Apr 02:10",
            "cst": "14 Apr 01:10",
            "mst": "14 Apr 00:10",
            "pst": "13 Apr 23:10",
        }
        self.assertEqual(self.r.get_start_all_timezones(), expected_timezone_dict)


if __name__ == "__main__":
    unittest.main()
