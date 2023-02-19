import random

events = {'Event': .6375, 'Shrine': .2125, 'Fight': .10, 'Shop': .03, 'Treasure': .02}

for key, value in events:
    print(value)

res = random.randint(.01, 1)
print(res)

for value in events:
    if res == events.values():
        print(events.key)