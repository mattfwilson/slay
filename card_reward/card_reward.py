import random
from defect_cards import *

drawCount = 10
upgradeChoice = (True, False)
upgraded = False
defectCards = [BallLightning(upgraded), ColdSnap(upgraded)]
hand = []

for count in range(drawCount):
    print(count)
    print(upgraded)
    upgraded = random.choice(upgradeChoice)
    hand.append(random.choice(defectCards))

for card in hand:
    print(card)