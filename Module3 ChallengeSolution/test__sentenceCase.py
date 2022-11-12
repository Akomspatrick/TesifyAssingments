import sentenceCase
import unittest
class TestSentencecase(unittest.TestCase):

    def testBaseIsraisedToExponential(self):
        self.assertTrue(sentenceCase.Sentencecase('this is Great'),'This is great')
        self.assertTrue(sentenceCase.Sentencecase('it is not ok'), 'It is not ok')


if __name__=='__main__':
    unittest.main()