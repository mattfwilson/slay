class GameState:
    def __init__(self):
        self.NAME = 'Karmae'
        self.MAX_HP = 72
        self.HP = self.MAX_HP
        self.MAX_ENERGY = 3
        self.ENERGY = self.MAX_ENERGY
        self.DECK = []
        self.START_ATTACK = 5
        self.START_BLOCK = 5
        self.START_DRAW = 2
        self.DRAW_PILE = []
        self.HAND = []
        self.DISCARD_PILE = []
        self.TURN_DRAW = 5
        self.CARD_DRAW = 0
        self.TURN_COUNT = 0
        self.FLOOR_COUNT = 0
        self.ENCOUNTER = []
        self.ACTIONS = ['Draw', 'Attack', 'Block', 'Discard', 'Draw Pile', 'Discard Pile']
        self.DEBUFFS = ['Vulnerable', 'Weakness', 'Frail']
        self.ATTACK = 0
        self.BLOCK = 0
        self.ENEMY_HP = 0
        self.ENEMY_INTENT = 0 # e.g. (1, 8) tuple from intent()
        self.ENEMY_BLOCK = 0 
        self.ENEMY_ATTACK = 0
        self.CARDS_PLAYED = 0

def showDraw():
    print(f'DRAW PILE:')
    print(state.DRAW_PILE)

def showHand():
    print(f'\nCURRENT HAND:')
    print(state.HAND)

def showDiscard():
    print(f'\nDISCARD PILE:')
    print(state.DISCARD_PILE)

def showPiles():
    print('-' * 50 + f' [PILES]')
    showDraw()
    showHand()
    showDiscard()

state = GameState()
print(state.START_DRAW)
