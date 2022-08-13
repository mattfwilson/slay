import unittest
from vars import *

class Test_Deck(unittest.TestCase):
    
    def test_HP(self):
        self.assertEqual(state.HP, 35)
        self.assertEqual(state.HP, state.MAX_HP)

    def test_energy(self):
        self.assertEqual(state.ENERGY, 3)
        self.asserEqual(state.ENERGY, state.MAX_ENERGY)

    def test_block(self):
        self.assertEqual(state.BLOCK, 0)

    def test_turn_draw(self):
        self.assertEqual(state.TURN_DRAW)

if __name__ == '__main__':
    unittest.main()