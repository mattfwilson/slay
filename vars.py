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
        self.FLOOR_COUNT = 0
        self.ENCOUNTER = []
        self.ACTIONS = ['Draw', 'Draw Pile', 'Attack', 'Block', 'Discard', 'Discard Pile']
        self.ATTACK = 0
        self.BLOCK = 0
        self.ENEMY_HP = 0
        self.ENEMY_INTENT = 0
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
    print('-' * 70 + f' [PILES]')
    showDraw()
    showHand()
    showDiscard()

state = GameState()