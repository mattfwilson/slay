import random

event_chance = {'Event': 64, 'Shrine': 21, 'Fight': 10, 'Shop': 3, 'Treasure': 2}
trials = 100

for trial in range(0, trials):
    for key, value in event_chance.items():
        roll = random.randint(0, 100)
        if roll <= value:
            print(key)
