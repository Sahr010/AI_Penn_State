import json
import os
import csv
from datetime import datetime

#https://github.com/CooperJRG/tetris-AI/blob/main/README.md

def save_heuristic(heuristic, filename="best_heuristic.json"):
    with open(filename, "w") as f:
        json.dump(heuristic, f)
    print(f"✅ Heuristic saved to {filename}")

def load_heuristic(filename="best_heuristic.json"):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            heuristic = json.load(f)
        print(f"📂 Loaded heuristic from {filename}")
        return heuristic
    else:
        print(f"⚠️ No saved heuristic found at {filename}")
        return None
    


def record_game_statistics(heuristic, high_score, lines_cleared, tot_lines_cleared, tetrises, game_overs, filename="game_stats.csv"):
    fieldnames = ['timestamp', 'high_score', 'lines_cleared', 'tot_lines_cleared', 'tetrises', 'game_overs'] + list(heuristic.keys())
    row = {
        'timestamp': datetime.now().isoformat(),
        'high_score': high_score,
        'lines_cleared': lines_cleared,
        'tot_lines_cleared': tot_lines_cleared,
        'tetrises': tetrises,
        'game_overs': game_overs,
        **heuristic
    }

    try:
        with open(filename, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if f.tell() == 0:
                writer.writeheader()
            writer.writerow(row)
        print(f"📊 Logged game stats to {filename}")
    except Exception as e:
        print(f"⚠️ Failed to log game stats: {e}")