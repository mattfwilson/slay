from load_runs import load_run_history
from load_runs import char_colors
from matplotlib import pyplot as plt

characters = ['THE_SILENT']

for char in characters:
    runs = load_run_history(char)
     
    floor_reach_count = {}

    for filename, data in runs.items():
        floor_reached = int(data.get('floor_reached'))

        if floor_reached is None:
            continue
        elif floor_reached not in floor_reach_count:
            floor_reach_count[floor_reached] = 1
        else:
            floor_reach_count[floor_reached] += 1

    print(floor_reach_count.items())

    labels = list(sorted(floor_reach_count.keys()))
    values = [floor_reach_count[floor_reached] for floor_reached in labels]

    plt.figure(figsize=(20, 12))
    
    bars = plt.bar(labels, values, color=char_colors.get(char))
    
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}', ha='center', va='bottom')

    plt.xticks(rotation=90, fontsize=8)
    plt.title(f'History of deaths by floor # ({sum(floor_reach_count.values())} total deaths on {char})')
    plt.xlabel('Floor #')
    plt.ylabel('Amount of Deaths')
    plt.tight_layout()
    plt.show()
    
