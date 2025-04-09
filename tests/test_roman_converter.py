import unittest
from src.roman_converter import decimal_to_roman

class TestRomanConverter(unittest.TestCase):

    def test_basic_numbers(self):
        self.assertEqual(decimal_to_roman(1), "I")
        self.assertEqual(decimal_to_roman(5), "V")
        self.assertEqual(decimal_to_roman(10), "X")
        self.assertEqual(decimal_to_roman(15), "XV")
        self.assertEqual(decimal_to_roman(20), "XX")
        self.assertEqual(decimal_to_roman(30), "XXX")

    def test_subtraction_rules(self):
        self.assertEqual(decimal_to_roman(4), "IV")
        self.assertEqual(decimal_to_roman(9), "IX")
        self.assertEqual(decimal_to_roman(40), "XL")
        self.assertEqual(decimal_to_roman(90), "XC")
        self.assertEqual(decimal_to_roman(400), "CD")
        self.assertEqual(decimal_to_roman(540), "DXL")
        self.assertEqual(decimal_to_roman(590), "DXC")
        self.assertEqual(decimal_to_roman(640), "DCXL")
        self.assertEqual(decimal_to_roman(690), "DCXC")
        self.assertEqual(decimal_to_roman(900),"CM")

    def test_complex_numbers(self):
        self.assertEqual(decimal_to_roman(49), "XLIX")
        self.assertEqual(decimal_to_roman(99), "XCIX")
        self.assertEqual(decimal_to_roman(149), "CXLIX")
        self.assertEqual(decimal_to_roman(499), "CDXCIX")
        self.assertEqual(decimal_to_roman(999), "CMXCIX")
        self.assertEqual(decimal_to_roman(1499), "MCDXCIX")
        self.assertEqual(decimal_to_roman(1999), "MCMXCIX")
        self.assertEqual(decimal_to_roman(2495), "MMCDXCV" )
        self.assertEqual(decimal_to_roman(3999), "MMMCMXCIX")

if __name__ == '__main__':
    unittest.main()