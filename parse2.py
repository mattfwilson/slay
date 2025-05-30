import json
from pathlib import Path
import matplotlib.pyplot as plt


runs_dir = Path("C:/Program Files (x86)/Steam/steamapps/common/SlayTheSpire/runs")
characters = ["DEFECT"]
card_picks: dict = {}

def load_run_history(character):
    folder = runs_dir / f"{character}/"
    runs: dict = {}

    for file in folder.iterdir():
        if file.is_file():
            try:
                with file.open("r", encoding="utf-8") as f:
                    try:
                        data = json.load(f)
                        print(f"{character} - {file.name} - \n\n{data}\n")
                        runs[file.name] = data
                    except json.JSONDecodeError:
                        f.seek(0)
                        file_runs = []
                        for line in f:
                            line = line.strip()
                            if line:
                                try:
                                    file_runs.append(json.loads(line))
                                except json.JSONDecodeError:
                                    print(f"Line in {file.name} is malformed.")
                        if file_runs:
                            runs[file.name] = file_runs
            except Exception as e:
                print(f"Error reading {file}: {e}")

    return runs
   

for char in characters:
    runs = load_run_history(char)
     
    for filename, data in runs.items():
        print(f"{filename}\n{data}\n")
        master_deck = data.get('master_deck')

        for card in master_deck:
            if data.get('victory') == True:
                if card not in card_picks:
                    card_picks[card] = 1
                else:
                    card_picks[card] += 1

        if isinstance(data, dict):
            print(f"Score: {data.get('score')} | Victory: {data.get('victory')} | Floor Reached: {data.get('floor_reached')} | Ascension Level: {data.get('ascension_level')}\n")
        elif isinstance(data, list):
            for i, run in enumerate(data):
                if isinstance(run, dict):
                    print("multiple embedded dicts")
                else:
                    print(f"[{filename} #{i}] Invalid run format: {run}\n")

sorted_res: dict = dict(sorted(card_picks.items(), key=lambda item: item[1], reverse=True))
starters = {'Strike_R', 'Defend_R', 'Strike_R+1', 'Defend_R+1', 'Strike_G', 'Defend_G', 'Strike_G+1', 'Defend_G+1', 'Strike_B', 'Defend_B', 'Strike_B+1', 'Defend_B+1', 'Strike_P', 'Defend_P', 'Strike_P+1', 'Defend_P+1'}
sorted_res = {key: val for key, val in sorted_res.items() if key not in starters}

for key, val in sorted_res.items():
        print(f'{key}: {val}')

labels = list(sorted_res.keys())
values = list(sorted_res.values())
max_values = max(values)

plt.figure(figsize=(20, 12))
bars = plt.bar(labels, values, color='green')
plt.ylim (0, max_values * 1.05)
plt.xticks(rotation=90, fontsize=8)

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2, height, f'{int(height)}', ha='center', va='bottom')

plt.title('Most Picked Cards in Successful Runs')
plt.xlabel('Card Picks')
plt.ylabel('Times Picked')
plt.tight_layout()
plt.show()

