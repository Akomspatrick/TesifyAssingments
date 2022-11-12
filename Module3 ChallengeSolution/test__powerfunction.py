import powerfunction
import unittest
class Testpowerfunc(unittest.TestCase):
    def testBaseIsraisedToExponential(self):
        self.assertTrue(powerfunction.powerfunc(2,3),8)
        self.assertTrue(powerfunction.powerfunc(3, 3), 27)


if __name__=='__main__':
    unittest.main()