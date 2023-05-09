import random
from defect_cards import *

drawCount = 10
upgraded = False
hand = []

seed = random.seed(4)
nested_seed = random.seed(seed)
print(nested_seed)

for count in range(drawCount):
    defectCards = [BallLightning(upgraded), ColdSnap(upgraded), Barrage(upgraded)]
    upgraded = random.choice([True, False])
    draw = random.choice(defectCards)
    hand.append(draw)

for card in hand:
    print(card)