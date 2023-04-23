import random
from defect_cards import *

drawCount = 10
upgradeChoice = (True, False)
upgraded = random.choice(upgradeChoice)
defectCards = [BallLightning(upgraded), ColdSnap(upgraded)]
hand = []

for count in range(drawCount):
    print(count)
    hand.append(random.choice(defectCards))

for card in hand:
    print(card)