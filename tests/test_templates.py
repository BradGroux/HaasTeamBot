# -*- coding: utf-8 -*-
import unittest

from .context import haasbot
import haasbot.template as t


class TemplateLoadTests(unittest.TestCase):
    """Basic template loading test cases."""

    def test_basic_template_load(self):
        loaded_template = t.load_template_file("test.md.tmpl", test_variable="test")
        expected_output = "# Test Thread Template\ntest"
        self.assertEqual(loaded_template, expected_output)


if __name__ == "__main__":
    unittest.main()
