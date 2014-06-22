from django.test import TestCase
from webapp.templatetags.color_code_calc import generate_color_code


class ColorCodingTest(TestCase):
    def test_color_code_large_number(self):
        actual = generate_color_code(100.32)
        expected = "success"
        self.assertEqual(actual, expected)

    def test_color_code_borderline(self):
        actual = generate_color_code(6.499999999)
        expected = "warning"
        self.assertEqual(actual, expected)
