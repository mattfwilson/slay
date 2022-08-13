import unittest
from slay import *

class Test_Deck(unittest.TestCase):
    
    def test_HP(self):
        self.assertGreater(state.HP, 35)

    def test_energy(self):
        self.assertEqual(state.ENERGY, 3)

    def test_name(self):
        if state.NAME is str():
            res = True
            self.assertTrue(res)

if __name__ == '__main__':
    unittest.main()