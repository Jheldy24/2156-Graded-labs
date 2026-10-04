from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "service_dispatches.csv"
OUTPUT_DIR = ROOT / "output"


def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    df = pd.read_csv(DATA_PATH)

    print(f"Rows (completed dispatches): {len(df)}")
    print(
        "Missing values in analysis fields:"
    )
    print(df[["job_difficulty_score", "technician_hours", "service_region"]].isna().sum())

    plt.figure(figsize=(8, 6))
    for region, region_df in df.groupby("service_region"):
        plt.scatter(
            region_df["job_difficulty_score"],
            region_df["technician_hours"],
            label=region,
            alpha=0.7,
        )
    plt.legend(title="Service Region")
    plt.title("Job Difficulty and Technician Hours")
    plt.xlabel("Job Difficulty Score")
    plt.ylabel("Technician Hours")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "dispatch_relationships.png", dpi=150)
    plt.close()
    region_summary = (
        df.groupby("service_region")["technician_hours"]
        .agg(count="count", mean="mean", median="median")
        .reset_index()
    )
    region_summary.to_csv(OUTPUT_DIR / "region_summary.csv", index=False)
    print(region_summary)

if __name__ == "__main__":
    main()
