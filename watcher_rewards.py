import random

reward_count = 3
inv = []
common_rate = 60
uncommon_rate = 37
rare_rate = 97
common = ['Consecrate', 'Crescendo', 'Bowling Bash', 'Sash Whip', 'Protect', 'Pressure Points', 'Third Eye', 'Tranquility', 'Prostrate', 'Just Lucky', 'Follow-Up', 'Flying Sleeves', 'Evaluate', 'Empty Fist', 'Empty Body', 'Cut Through Fate', 'Crush Joints']
uncommon = ['Carve Reality', 'Collect', 'Battle Hymn', 'Conclude', 'Deceive Reality', 'Fasting', 'Foreign Influence', 'Empty Mind', 'Mental Fortress', 'Wreath of Flame', 'Worship', 'Windmill Strike', 'Wheel Kick', 'Weave', 'Wave of the Hand', 'Wallop', 'Tantrum', 'Talk to the Hand', 'Swivel', 'Study', 'Signature Move', 'Sands of Time', 'Sanctity', 'Rushdown', 'Reach Heaven', 'Perserverance', 'Pray', 'Niravan', 'Meditate', 'Like Water', 'Inner Peace', 'Indignation', 'Foresight', 'Fear No Evil', 'Fear No Evil', ]
rare = ['Ragnarok', 'Alpha', 'Blasphemy', 'Conjure Blade', 'Deva Form', 'Establishment', 'Deus Ex Machina', 'Devotion', 'Judgement', 'Lesson Learned', 'master Reality', 'Omniscience', 'Scrawl', 'Spirit Shield', 'Vault', 'Wish', '']

for i in range(reward_count):
    reward = random.randint(1, 100)
    if reward > 37 and reward <= 97:
        reward = random.choice(common)
        print(f'COMMON: {reward}')
    elif reward <= 37:
        reward = random.choice(uncommon)
        print(f'UNCOMMON: {reward}')
    elif reward > 97:
        reward = random.choice(rare)
        print(f'RARE: {reward}')
