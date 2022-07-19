# player
NAME = 'You'
HP = 54
MAX_HP = 54
# ENERGY = 3
MAX_ENERGY = 3
DRAW_COUNT = 5
HAND = [] # doesn't need to be global
DRAW_PILE = [] # doesn't need to be global
DISCARD_PILE = [] # doesn't need to be global

# combat
ENEMY = []
COMBAT_COUNT = 1
TURN_COUNT = 0
ACTIONS = ['Draw', 'Attack', 'Block', 'Draw Pile', 'Discard Pile']

# # misc
# COUNTER = 10 # for testPool() function

class GameState:
    def __init__(self):
        self.NAME = 'You'
        self.HP = 50
        self.MAX_HP = 50
        self.ENERGY = 3
        self.MAX_ENERGY = 3
        self.DECK = []
        self.DRAW_PILE = []
        self.HAND = []
        self.DISCARD_PILE = []
        self.DRAW_COUNT = 5
        self.TURN_COUNT = 0
        self.COMBAT_COUNT = 0
        self.ENCOUNTER = []
        self.ACTIONS = ['Draw', 'Attack', 'Block', 'Draw Pile', 'Discard Pile']

state = GameState()