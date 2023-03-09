import unittest

from translator import frenchToEnglish, englishToFrench


class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')


unittest.main()
