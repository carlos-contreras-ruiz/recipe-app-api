from django.test import TestCase

from app.calc import add, subtract

class CalcTests(TestCase):

    def test_add_number(self):
        """Test that 2 numbers are added"""
        self.assertEqual(add(3,8), 11)

    def test_subtract_numbers(self):
        """"TDD example substraction"""
        self.assertEqual(subtract(5,11), 6)
