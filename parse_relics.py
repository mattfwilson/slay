from starters import starters
from load_runs import load_run_history
from matplotlib import pyplot as plt

characters = ['IRONCLAD']
char_colors = {'IRONCLAD': 'red', 'THE_SILENT': 'green', 'DEFECT': 'skyblue', 'WATCHER': 'purple'}
relic_picks: dict = {}

for char in characters:
    runs = load_run_history(char)
     
    for filename, data in runs.items():
        print(f'{filename}\n{data}\n')
        relics = data.get('master_deck')

        for relic in relics:
            if data.get('victory') == True:
                if relic not in relic_picks:
                    relic_picks[relic] = 1
                else:
                    relic_picks[relic] += 1

        if isinstance(data, dict):
            print(f"Score: {data.get('score')} | Victory: {data.get('victory')} | Floor Reached: {data.get('floor_reached')} | Ascension Level: {data.get('ascension_level')}\n")
        elif isinstance(data, list):
            for i, run in enumerate(data):
                if isinstance(run, dict):
                    print('multiple embedded dicts')
                else:
                    print(f'[{filename} #{i}] Invalid run format: {run}\n')

    for key, val in relic_picks.items():
            print(f'{key}: {val}')

    labels = list(relic_picks.keys())
    values = list(relic_picks.values())
    max_values = max(values)
    plt.figure(figsize=(20, 12))
    
    bars = plt.bar(labels, values, color=char_colors.get(char))
    
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}', ha='center', va='bottom')

    plt.ylim (0, max_values * 1.05)
    plt.xticks(rotation=90, fontsize=8)
    plt.title('Most Picked Cards in Successful Runs')
    plt.xlabel('Card Picks')
    plt.ylabel('# Times Picked')
    plt.tight_layout()
    plt.show()
