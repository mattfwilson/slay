from load_runs import load_run_history
from matplotlib import pyplot as plt
from collections import Counter

characters = ['DEFECT']
char_colors = {'IRONCLAD': 'red', 'THE_SILENT': 'green', 'DEFECT': 'skyblue', 'WATCHER': 'purple'}
floor_death: dict = {}

for char in characters:
    runs = load_run_history(char)
     
    for filename, data in runs.items():
        floor_reached = data.get('floor_reached')
        print(floor_reached)

        if floor_reached not in floor_death:
            floor_death[floor_reached] = 1
        else:
            floor_death[floor_reached] += 1
        

        if isinstance(data, dict):
            print('is dict')
        elif isinstance(data, list):
            print('is list')
            for runid, run in enumerate(data):
                if isinstance(run, dict):
                    print(f'multiple embedded dicts: [{filename} #{runid}] Invalid run format: {run}\n')
                else:
                    print(f'[{filename} #{runid}] Invalid run format: {run}\n')

    sorted_res: dict = dict(sorted(floor_death.items(), key=lambda item: item[1], reverse=True))

    labels = list(sorted_res.keys())
    values = list(sorted_res.values())
    max_values = max(values)
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

