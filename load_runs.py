import json
from pathlib import Path

runs_dir = Path("C:/Program Files (x86)/Steam/steamapps/common/SlayTheSpire/runs")

def load_run_history(character):
    folder = runs_dir / f"{character}/"
    runs: dict = {}

    for file in folder.iterdir():
        if not file.is_file():
            continue

        try:
            with file.open("r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
#                    print(f"{character} - {file.name} - \n\n{data}\n")
                    runs[file.name] = data
                except json.JSONDecodeError:
                    return runs

        except Exception as e:
            print(f"Error reading {file}: {e}")

    return runs
