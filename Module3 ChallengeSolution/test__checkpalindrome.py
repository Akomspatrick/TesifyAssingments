import palindrome
import unittest
class Testpalindrome(unittest.TestCase):
    def testBaseIsraisedToExponential(self):
        self.assertTrue(palindrome.checkpalindrome("ABABA"))
        self.assertTrue(palindrome.checkpalindrome("ABADBA"))


if __name__=='__main__':
    unittest.main()