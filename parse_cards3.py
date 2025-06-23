from starters import starters
from load_runs import load_run_history
from load_runs import char_colors
from matplotlib import pyplot as plt

characters = ['DEFECT']
card_picks: dict = {}

for char in characters:
    runs = load_run_history(char)
     
    for filename, data in runs.items():
        print(f'{filename}\n{data}\n')
        master_deck = data.get('master_deck')

        for card in master_deck:
            if card not in card_picks:
                card_picks[card] = 1
            else:
                card_picks[card] += 1

        if isinstance(data, dict):
            print(f"Score: {data.get('score')} | Victory: {data.get('victory')} | Floor Reached: {data.get('floor_reached')} | Ascension Level: {data.get('ascension_level')}\n")
        elif isinstance(data, list):
            for i, run in enumerate(data):
                if isinstance(run, dict):
                    print('multiple embedded dicts')
                else:
                    print(f'[{filename} #{i}] Invalid run format: {run}\n')

    sorted_res = {key: val for key, val in sorted(((k, v) for k, v in card_picks.items() if k not in starters and v > 10), key=lambda item: item[1], reverse=True)}

    for key, val in sorted_res.items():
            print(f'{key}: {val}')

    labels = list(sorted_res.keys())
    values = list(sorted_res.values())
    print(values)

    if values:
        max_values = max(values)
    else:
        print('No card values > 1 to plot')
        continue

    plt.figure(figsize=(20, 12))
    color = char_colors.get(char, 'gray') 
    bars = plt.bar(labels, values, color=color)
    
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

