class GameState:
    def __init__(self):
        self.NAME = 'You'
        self.HP = 50
        self.MAX_HP = 50
        self.ENERGY = 3
        self.MAX_ENERGY = 3
        self.BLOCK = 0
        self.DECK = []
        self.DRAW_PILE = []
        self.HAND = []
        self.DISCARD_PILE = []
        self.DRAW_COUNT = 5
        self.TURN_COUNT = 0
        self.COMBAT_COUNT = 0
        self.ENCOUNTER = []
        self.ACTIONS = ['Draw', 'Draw Pile', 'Attack', 'Block', 'Discard', 'Discard Pile']

state = GameState()