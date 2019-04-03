# -*- coding: utf-8 -*-

from .context import haasbot
import haasbot.template as t

import unittest


class TemplateLoadTests(unittest.TestCase):
    """Basic template loading test cases."""

    def test_basic_template_load(self):
        template_loader = t.ThreadTemplate(filename="test.md.tmpl")
        loaded_template = template_loader.load(test_variable="test")
        expected_output = "# Test Thread Template\ntest"
        self.assertEqual(loaded_template, expected_output)


if __name__ == "__main__":
    unittest.main()
