import random

event_chance = {'Event': .6375, 'Shrine': .2125, 'Fight': .10, 'Shop': .03, 'Treasure': .02}

# for key, value in event_chance:
#     print(value)

res = random.randint(.01, 1)
print(res)

for value in event_chance:
    if res == event_chance.values():
        print(event_chance.key)