import random
from defect_cards import *

deckCount = 10
drawCount = 5
upgraded = False
deck = []
hand = []

seed = random.seed(4)
nested_seed = random.seed(seed)
print(nested_seed)

for count in range(deckCount):
    defectCards = [BallLightning(upgraded), ColdSnap(upgraded), Barrage(upgraded)]
    upgraded = random.choice([True, False])
    draw = random.choice(defectCards)
    deck.append(draw)

for card in deck:
    print(card)

for card in deck:
    hand.append(card)
print(f'Your hand: {hand}')

    