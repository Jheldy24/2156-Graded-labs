from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "clinic_waits.csv"
OUTPUT_DIR = ROOT / "output"


def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    df = pd.read_csv(DATA_PATH)

    # TODO 1: Document the row grain in output/decision_note.md.
    # TODO 2: Check missingness in site and wait_minutes.
    # TODO 3: Build site_wait_summary.csv with count, mean, and median.
    # TODO 4: Build wait_time_by_site.png with honest labels and a zero baseline.
    # TODO 5: Include the visit count in the chart or an adjacent table.
    # TODO 6: Write a bounded decision note with one limitation.

    print(df.head())
    print(df[["site", "wait_minutes"]].isna().sum())


if __name__ == "__main__":
    main()
