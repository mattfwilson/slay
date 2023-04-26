import random
from defect_cards import *

drawCount = 10
upgraded = random.choice([True, False])
defectCards = [BallLightning(upgraded), ColdSnap(upgraded)]
hand = []

for count in range(drawCount):
    print(count)
    print(upgraded)
    draw = random.choice(defectCards)
    res = hand.append(draw)

for card in hand:
    print(card)