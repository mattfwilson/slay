import unittest
from slay import *

class Test_Deck(unittest.TestCase):
    
    def test_buildDeck(self):
        totalDraw = state.START_ATTACK, state.START_BLOCK, state.START_DRAW
        self.assertEqual(totalDraw, 10)

if __name__ == '__main__':
    unittest.main()
