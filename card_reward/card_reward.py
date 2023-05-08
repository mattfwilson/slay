import random
from defect_cards import *

drawCount = 10
upgraded = False
hand = []

random.seed(4)

for count in range(drawCount):
    defectCards = [BallLightning(upgraded), ColdSnap(upgraded), Barrage(upgraded)]
    upgraded = random.choice([True, False])
    draw = random.choice(defectCards)
    hand.append(draw)

for card in hand:
    print(card)