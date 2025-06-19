from load_runs import load_run_history
from matplotlib import pyplot as plt

characters = ['DEFECT']
char_colors = {'IRONCLAD': 'red', 'THE_SILENT': 'green', 'DEFECT': 'skyblue', 'WATCHER': 'purple'}

for char in characters:
    runs = load_run_history(char)
     
    floor_reach_count = []

    for filename, data in runs.items():
        floor_reached = int(data.get('floor_reached'))

        if floor_reached is None:
            continue
        
        floor_reach_count.append(floor_reached)

    labels = floor_reach_count
    values = floor_reach_count

    plt.figure(figsize=(20, 12))
    
    bars = plt.bar(labels, values, color=char_colors.get(char))
    
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}', ha='center', va='bottom')

    plt.xticks(rotation=90, fontsize=8)
    plt.title('History of deaths by floor #')
    plt.xlabel('Run History')
    plt.ylabel('Floor Died On')
    plt.tight_layout()
    plt.show()
    
