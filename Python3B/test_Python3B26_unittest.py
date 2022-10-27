import Python3B26
import unittest

class TestPython3B26(unittest.TestCase) :

    def test_StringCompare_TwoEqualString(self):
        self.assertTrue(Python3B26.StringCompare('4','4'),True)

    def test_StringCompare_TwoNonStringShoulBefalse(self):
        self.assertFalse(Python3B26.StringCompare('4',4),False)

    def test_StringCompareTwoNumberShouldBeFalse(self):
        self.assertFalse(Python3B26.StringCompare(4,4),False)

    def test_StringCompare_TwoEqualNumber_Shouldbefalse(self):
        self.assertTrue(Python3B26.NumberCompare(4,4),True)

    def test_StringCompare_TwoDiffNumShoulBefalse(self):
        self.assertFalse(Python3B26.NumberCompare(5,4),False)

    def test_StringCompareTwoDiffDataTypesBeFalse(self):
        self.assertFalse(Python3B26.NumberCompare('4',4),False)