import json
from pathlib import Path
import os

runs_dir = Path("C:/Program Files (x86)/Steam/steamapps/common/SlayTheSpire/runs")

characters = ["IRONCLAD", "THE_SILENT"]

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
            print(card)

        if isinstance(data, dict):
            print(f"Score: {data.get('score')} | Victory: {data.get('victory')} | Floor Reached: {data.get('floor_reached')} | Ascension Level: {data.get('ascension_level')}\n")
        elif isinstance(data, list):
            for i, run in enumerate(data):
                if isinstance(run, dict):
                    print(f"[{filename} #{i}] Score: {run.get('score')} | Victory: {run.get('victory')} | Floor Reached: {run.get('floor_reached')} | Ascension Level: {data.get('ascension_level')}\n")
                else:
                    print(f"[{filename} #{i}] Invalid run format: {run}\n")

