import random

event_chance = {
    'Event': 64,
    'Shrine': 21,
    'Fight': 10,
    'Shop': 3,
    'Treasure': 2
}

test_dict = {
    None: 'a',
    (1, 2): 'b',
    True: 'c'
}

trials = 25

for trial in range(0, trials):
    for key, value in event_chance.items():
        roll = random.randint(1, 100)
        if roll <= value:
            print(key)

my_tuple = ((1, 1), (2, 2), (1, 2))

for key in test_dict:
    if (key == (1, 2)):
        print(test_dict.get(key))
    else:
        print('Not in dictionary!')