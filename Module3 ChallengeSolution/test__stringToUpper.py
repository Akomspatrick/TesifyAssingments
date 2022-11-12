import stringToUpper
import unittest
class TeststringToUpper(unittest.TestCase):
    def testBaseIsraisedToExponential(self):
        self.assertTrue(stringToUpper.covertToUpper("Ade"),"ADE")
        self.assertTrue(stringToUpper.covertToUpper("hil"),"hil")


if __name__=='__main__':
    unittest.main()