import random

event_chance = {'Event': .6375, 'Shrine': .2125, 'Fight': .10, 'Shop': .03, 'Treasure': .02}

res = random.randint(1, 100)
print(res)

for value in event_chance:
    if res == event_chance.values():
        print(event_chance.key)