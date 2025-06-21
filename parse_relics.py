from starters import starters
from load_runs import load_run_history
from load_runs import char_colors
from matplotlib import pyplot as plt

characters = ['DEFECT']
char_colors = {'IRONCLAD': 'red', 'THE_SILENT': 'green', 'DEFECT': 'skyblue', 'WATCHER': 'purple'}
relic_picks: dict = {}

for char in characters:
    runs = load_run_history(char)
     
    for filename, data in runs.items():
        relics = data.get('relics')

        for relic in relics:
            if data.get('victory') == True:
                if relic not in relic_picks:
                    relic_picks[relic] = 1
                else:
                    relic_picks[relic] += 1

        if isinstance(data, dict):
            print('is dict')
        elif isinstance(data, list):
            print('is list')
            for runid, run in enumerate(data):
                if isinstance(run, dict):
                    print(f'multiple embedded dicts: [{filename} #{runid}] Invalid run format: {run}\n')
                else:
                    print(f'[{filename} #{runid}] Invalid run format: {run}\n')

    sorted_res: dict = dict(sorted(relic_picks.items(), key=lambda item: item[1], reverse=True))
    sorted_res = {key: val for key, val in sorted_res.items() if key not in starters}
    
    for key, val in relic_picks.items():
            print(f'{key}: {val}')

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
    plt.title('Most Picked Relics in Successful Runs')
    plt.xlabel('Relics Picks')
    plt.ylabel('# Times Picked')
    plt.tight_layout()
    plt.show()

