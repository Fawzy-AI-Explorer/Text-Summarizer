"""functions for reading and writing files in various formats."""

import os
from typing import List, Dict
import json
import random
import pandas as pd


def read_file(path: str, print_log: bool = False) -> pd.DataFrame:
    """Reads a file and returns a pandas DataFrame."""
    if print_log:
        print(f"[INFO] Reading file {path}...")
    df = None
    if path:
        df = pd.read_csv(path)
    return df

def save_to_file(save_dir, save_file_name: str, df: pd.DataFrame, print_log: bool = True):
    """Saves a pandas DataFrame to a CSV file in the 'data/processed' directory."""
    if print_log:
        print(f"[INFO] Saving DataFrame to file {save_file_name}...")

    os.makedirs(os.path.join('Data', save_dir), exist_ok=True)
    _save_path = os.path.join('Data', 'processed', f"{save_file_name}.csv")
    df.to_csv(
        path_or_buf=_save_path
    )


def save_json_file(save_file_name: str, obj: List[Dict]):
    """Saves a list of dictionaries to a JSON lines file."""

    save_dir = os.path.join('Data', 'annotations')
    os.makedirs(save_dir, exist_ok=True)

    save_path = os.path.join(save_dir, f"{save_file_name}.jsonl")

    with open(file=save_path, mode='w', encoding='utf-8') as f:
        for line in obj:
            json_string = json.dumps(line)
            f.write(json_string + '\n')
    print(f"[INFO] Saved to file {save_path}...")


def read_json_lines(path: str, shuffle: bool = True):
    """Reads a JSON lines file and returns a list of dictionaries. """
    print(f"\n[INFO] READING JSON line from file {path}...")
    raw_data = []
    with open(file=path, mode='r', encoding='utf-8') as f:
        for line in f.readlines():
            if line.strip() == "":
                continue

            raw_data.append(json.loads(line.strip()))
    if shuffle:
        random.Random(42).shuffle(raw_data)
    return raw_data
