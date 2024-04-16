import random

event_chance = {
    'Event': 64,
    'Shrine': 21,
    'Fight': 10,
    'Shop': 3,
    'Treasure': 2
}

trials = 100
trial_res = {
    'Event': 0,
    'Shrine': 0,
    'Fight': 0,
    'Shop': 0,
    'Treasure': 0
}

for trial in range(0, trials):
    for key, value in event_chance.items():
        roll = random.randint(1, 100)
        if roll <= value:
            if key == 'Event':
                trial_res['Event'] += 1
            elif key == 'Shrine':
                trial_res['Shrine'] += 1
            elif key == 'Fight':
                trial_res['Fight'] += 1
            elif key == 'Shop':
                trial_res['Shop'] += 1
            elif key == 'Treasure':
                trial_res['Treasure'] += 1
            print(key)

print(trial_res)
