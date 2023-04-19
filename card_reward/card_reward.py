import random
from collections import deque
from defect_cards import *

drawCount = 5
upgradeCard = (True, False)
upgraded = False
defectCards = [BallLightning(upgraded), ColdSnap(upgraded)]
hand = deque()

for count in range(drawCount):
    drawUpgrade = random.choice(upgradeCard)
    print(drawUpgrade)
    if drawUpgrade == True:
        upgraded = True
    else:
        upgraded = False
    hand.append(random.choice(defectCards))

for card in hand:
    print(card)
print(type(hand))