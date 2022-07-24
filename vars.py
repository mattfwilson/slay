import random

class GameState:
    def __init__(self):
        self.NAME = 'You'
        self.HP = 50
        self.MAX_HP = 50
        self.ENERGY = 7
        self.MAX_ENERGY = 7
        self.BLOCK = 0
        self.DECK = []
        self.DRAW_PILE = []
        self.HAND = []
        self.DISCARD_PILE = []
        self.DRAW_COUNT = 3
        self.TURN_COUNT = 0
        self.COMBAT_COUNT = 0
        self.ENCOUNTER = []
        self.ACTIONS = ['Draw', 'Draw Pile', 'Attack', 'Block', 'Discard', 'Discard Pile']
        self.PLAYER_DMG = 0
        self.BLOCK = 0
        self.ENEMY_BLOCK = 0
        self.ENEMY_DMG = 0
        self.CARDS_PLAYED = 0


def showDraw():
    print(f'\nDRAW PILE:')
    # for card in state.DRAW_PILE:
    # print(card.getSummary())
    print(state.DRAW_PILE)

def showHand():
    print(f'\nCURRENT HAND:')
    # for card in state.HAND:
    #     print(card.getSummary())
    print(state.HAND)

def showDiscard():
    print(f'\nDISCARD PILE:')
    # for card in state.DISCARD_PILE:
    #     print(card.getSummary())
    print(state.DISCARD_PILE)

def showPiles():
    showDraw()
    showHand()
    showDiscard()

state = GameState()