import unittest
from slay import *

class TestSlay(unittest.TestCase):
    
    def test_buildDeck(self):
        result = 5 + 3 + 2
        self.assertEqual(result, 10)

if __name__ == '__main__':
    unittest.main()