from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "delivery_delays.csv"
OUTPUT = ROOT / "output"
REQUIRED_COLUMNS = {
    "delivery_id",
    "delivery_window",
    "route_type",
    "delay_minutes",
    "package_weight_kg",
}


def load_and_validate() -> pd.DataFrame:
    """Load the authorized fictional data and complete basic integrity checks."""
    deliveries = pd.read_csv(DATA_FILE)
    assert set(deliveries.columns) == REQUIRED_COLUMNS, "Unexpected CSV columns."
    assert deliveries["delivery_id"].notna().all(), "delivery_id cannot be blank."
    assert deliveries["delivery_id"].is_unique, "delivery_id values must be unique."
    deliveries["delay_minutes"] = pd.to_numeric(deliveries["delay_minutes"], errors="coerce")
    return deliveries


def write_starter_profile(deliveries: pd.DataFrame) -> None:
    """Create starter evidence only; this is not the completed lab analysis."""
    profile = pd.DataFrame({
        "column": deliveries.columns,
        "rows": len(deliveries),
        "missing_values": [int(deliveries[column].isna().sum()) for column in deliveries.columns],
        "distinct_values": [int(deliveries[column].nunique(dropna=True)) for column in deliveries.columns],
    })
    profile.to_csv(OUTPUT / "starter_profile.csv", index=False)


def build_delay_summary(deliveries: pd.DataFrame) -> pd.DataFrame:
    delay_values = deliveries["delay_minutes"].dropna()
    q1 = float(delay_values.quantile(0.25))
    q3 = float(delay_values.quantile(0.75))
    iqr = q3 - q1
    summary = pd.DataFrame(
        {
            "usable_row_count": [int(len(delay_values))],
            "mean_delay_minutes": [float(delay_values.mean())],
            "median_delay_minutes": [float(delay_values.median())],
            "min_delay_minutes": [float(delay_values.min())],
            "max_delay_minutes": [float(delay_values.max())],
            "q1_delay_minutes": [q1],
            "q3_delay_minutes": [q3],
            "iqr_delay_minutes": [iqr],
            "missing_delay_values": [int(deliveries["delay_minutes"].isna().sum())],
        }
    )
    return summary


def save_delay_summary(deliveries: pd.DataFrame) -> None:
    build_delay_summary(deliveries).to_csv(OUTPUT / "delay_summary.csv", index=False)


def save_possible_high_delays(deliveries: pd.DataFrame) -> None:
    delay_values = deliveries["delay_minutes"].dropna()
    q1 = float(delay_values.quantile(0.25))
    q3 = float(delay_values.quantile(0.75))
    upper_fence = q3 + 1.5 * (q3 - q1)
    flagged = deliveries.loc[deliveries["delay_minutes"] > upper_fence, [
        "delivery_id",
        "delivery_window",
        "route_type",
        "delay_minutes",
        "package_weight_kg",
    ]].copy()
    flagged = flagged.sort_values("delay_minutes", ascending=False).reset_index(drop=True)
    flagged["upper_fence_minutes"] = upper_fence
    flagged = flagged[[
        "delivery_id",
        "delivery_window",
        "route_type",
        "delay_minutes",
        "package_weight_kg",
        "upper_fence_minutes",
    ]]
    flagged.to_csv(OUTPUT / "possible_high_delays.csv", index=False)


def plot_delay_distribution(deliveries: pd.DataFrame) -> None:
    delay_values = deliveries["delay_minutes"].dropna()
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))

    axes[0].hist(delay_values, bins=8, color="#4c72b0", edgecolor="black")
    axes[0].set_title("Delivery-stop delay distribution")
    axes[0].set_xlabel("Delay (minutes)")
    axes[0].set_ylabel("Count")

    axes[1].boxplot(
        delay_values,
        patch_artist=True,
        boxprops={"facecolor": "#8ecae6"},
        orientation="horizontal",
    )
    axes[1].set_title("Delay box plot")
    axes[1].set_xlabel("Delay (minutes)")
    axes[1].set_yticks([])

    fig.tight_layout()
    fig.savefig(OUTPUT / "delay_charts.png", dpi=200)
    plt.close(fig)


def build_delivery_window_summary(deliveries: pd.DataFrame) -> pd.DataFrame:
    counts = deliveries["delivery_window"].value_counts().reindex(["Morning", "Afternoon", "Evening"], fill_value=0)
    summary = counts.rename_axis("delivery_window").reset_index(name="count")
    summary["share"] = summary["count"] / summary["count"].sum()
    return summary


def save_independent_window_analysis(deliveries: pd.DataFrame) -> None:
    window_summary = build_delivery_window_summary(deliveries)
    window_summary.to_csv(OUTPUT / "delivery_window_summary.csv", index=False)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(window_summary["delivery_window"], window_summary["count"], color=["#4c72b0", "#55a868", "#c44e52"])
    ax.set_title("Delivery-stop counts by service window")
    ax.set_xlabel("Delivery window")
    ax.set_ylabel("Number of stops")
    fig.tight_layout()
    fig.savefig(OUTPUT / "delivery_window_chart.png", dpi=200)
    plt.close(fig)


def write_decision_note() -> None:
    note = (
        "## Guided interpretation\n\n"
        "Each row represents one completed delivery stop. Of the 22 records, 21 have a recorded delay and one is missing. The median delay is 22 minutes, so half of usable stops were delayed by 22 minutes or less; the mean is 32.9 minutes, notably higher than the median. This difference, together with the long upper tail, indicates a right-skewed distribution: most delays are below 40 minutes, while a few are much longer. The IQR is 27 minutes and the 79.5-minute upper fence flags DL-020 (95 minutes) and DL-021 (140 minutes) for review. These are possible unusual values, not automatically errors, and should remain in the dataset. Before reporting routine performance, verify those records and investigate the missing delay. This small descriptive dataset summarizes observed stops, but cannot establish why delays occurred or represent future performance.\n\n"
        "## Independent interpretation\n\n"
        "Delivery window is categorical, so counts and shares, shown in a bar chart, describe how stops are distributed without implying numerical distances between categories. Morning accounts for 8 of 22 stops (36.4%); Afternoon and Evening each account for 7 (31.8%). The counts are similar, so no service window dominates this dataset. A practical next step is to use these counts as context when planning and reporting stop volume, and gather more observations before drawing broader conclusions. This chart describes stop volume only: it does not summarize delays within each window or explain causes. The sample contains just 22 fictional stops, so these proportions may not represent other periods.\n"
    )
    (ROOT / "decision_note.md").write_text(note, encoding="utf-8")


def main() -> None:
    OUTPUT.mkdir(exist_ok=True)
    deliveries = load_and_validate()
    write_starter_profile(deliveries)
    save_delay_summary(deliveries)
    save_possible_high_delays(deliveries)
    plot_delay_distribution(deliveries)
    save_independent_window_analysis(deliveries)
    write_decision_note()
    print(f"Starter checks passed for {len(deliveries)} fictional delivery-stop records.")
    print("Created output/starter_profile.csv.")
    print("Created output/delay_summary.csv, output/possible_high_delays.csv, and output/delay_charts.png.")
    print("Created output/delivery_window_summary.csv and output/delivery_window_chart.png.")
    print("Completed decision_note.md.")


if __name__ == "__main__":
    main()
