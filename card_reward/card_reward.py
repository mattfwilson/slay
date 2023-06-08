import random
from defect_cards import *

deckCount = 10
drawCount = 5
upgraded = False
deck = []
hand = []

for count in range(deckCount):
    defectCards = [BallLightning(upgraded), ColdSnap(upgraded), Barrage(upgraded)]
    upgraded = random.choice([True, False])
    draw = random.choice(defectCards)
    deck.append(draw)

for card in range(drawCount):
    drawn = deck.pop(-1)
    hand.append(drawn)

print(f'\nYour hand:')
for card in hand:
    print(card)

print(f'\nDraw pile:')
for card in deck:
    print(card)

# Test 2
