"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Test adding numbers together."""
        rest = calc.add(5, 6)

        self.assertEqual(rest, 11)

    def test_subtract_numbers(self):
        """Test subtract numbers together."""
        rest = calc.subtract(10, 15)

        self.assertEqual(rest, 5)
