import json
from pathlib import Path
import os

runs_dir = Path("C:/Program Files (x86)/Steam/steamapps/common/SlayTheSpire/runs")

characters = ['IRONCLAD', 'THE_SILENT', 'DEFECT', 'WATCHER']

def load_run_history(character):
    file_path = runs_dir / f"{character}.run"
    if not file_path.exists():
        return f'path does not exists'

    print(file_path)
    
    try:
        with file_path.open("r", encoding="utf-8") as f:
            print(f'{f} opened')
            try:
                print(f'{f} loaded')
                return json.load(f)
            except json.JSONDecodeError:
                print('JSONDecodeError')
                f.seek(0)
                return [json.loads(line) for line in f if line.strip()]
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return []

for char in characters:
#    char_history = runs_dir / f"{char}/"
#    run_count = sum(1 for entry in os.scandir(char_history) if entry.is_file())
#    print(f"--- {char} has {run_count} runs ---")

    runs = load_run_history(char)
    print(f"--- {char} has {len(runs)} runs --- {runs}")
    
#    for run in runs:
#        print(f"Score: {run.get('score')} | Victory: {run.get('victory')} | Floor Reached: {run.get('floor_reached')}")
