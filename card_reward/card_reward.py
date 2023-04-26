import random
from defect_cards import *

drawCount = 10
upgraded = False
defectCards = [BallLightning(upgraded), ColdSnap(upgraded)]
hand = []

for count in range(drawCount):
    upgraded = random.choice([True, False])
    draw = random.choice(defectCards)
    hand.append(draw)

for card in hand:
    print(card)