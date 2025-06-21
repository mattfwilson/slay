from load_runs import load_run_history
from load_runs import char_colors
from matplotlib import pyplot as plt

characters = ['DEFECT']

for char in characters:
    runs = load_run_history(char)
     
    floor_reach_count = {}

    for filename, data in runs.items():
        floor_reached = int(data.get('floor_reached'))

        if floor_reached is None:
            continue
        
        floor_reach_count[floor_reached] = floor_reach_count.get(floor_reached, 0) + 1

    sorted_res = dict(sorted(floor_reach_count.items(), key=lambda item: item[1], reverse=True))
    labels = list(sorted_res.keys())
    values = list(sorted_res.values())
    print(values)
    
    max_values = max(values) if values else 0
    plt.figure(figsize=(20, 12))
    
    bars = plt.bar(labels, values, color=char_colors.get(char))
    
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}', ha='center', va='bottom')

    plt.ylim (0, max_values * 1.05)
    plt.xticks(rotation=90, fontsize=8)
    plt.title('Death by floor #')
    plt.xlabel('Floor #')
    plt.ylabel('Times died on floor')
    plt.tight_layout()
    plt.show()
    
