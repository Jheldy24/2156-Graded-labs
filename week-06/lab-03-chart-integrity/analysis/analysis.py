from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "clinic_waits.csv"
OUTPUT_DIR = ROOT / "output"


def build_summary(df: pd.DataFrame) -> pd.DataFrame:
    summary = (
        df.groupby("site", as_index=False)["wait_minutes"]
        .agg(
            count="size",
            mean_wait_minutes="mean",
            median_wait_minutes="median",
        )
        .sort_values("site")
    )
    summary["mean_wait_minutes"] = summary["mean_wait_minutes"].round(2)
    summary["median_wait_minutes"] = summary["median_wait_minutes"].round(2)
    return summary


def build_chart(summary: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(8, 5.5))
    colors = ["#4C78A8", "#F58518", "#54A24B"]
    bars = ax.bar(summary["site"], summary["mean_wait_minutes"], color=colors, edgecolor="black")

    ax.axhline(0, color="black", linewidth=1)
    ax.set_title("Average patient wait time by clinic site, April 2026")
    ax.set_xlabel("Clinic site")
    ax.set_ylabel("Average wait time (minutes)")
    ax.set_ylim(0, max(summary["mean_wait_minutes"].max() * 1.25, 10))
    ax.grid(axis="y", linestyle="--", linewidth=0.5, alpha=0.4)

    for bar, value, count in zip(bars, summary["mean_wait_minutes"], summary["count"]):
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + 1.5,
            f"{value:.1f} min",
            ha="center",
            va="bottom",
            fontsize=10,
        )
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            1.8,
            f"n={count}",
            ha="center",
            va="bottom",
            fontsize=9,
            color="dimgray",
        )

    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "wait_time_by_site.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


def write_decision_note() -> None:
    note = """# Decision note for clinic operations briefing

One completed patient visit is the row grain in `data/clinic_waits.csv`. Each record represents one visit at a clinic site, and there are no missing values in the analysis fields (`site` and `wait_minutes`). The site summary shows that North had the longest average wait time at 38.0 minutes, compared with South at 28.7 minutes and Central at 22.2 minutes. The median wait times follow the same pattern, which suggests the difference is not driven by a single outlier visit.

The most practical next step is to review patient-flow processes at the North site, starting with a short audit of check-in, rooming, and provider-start delays by appointment type and day. That review should be targeted to the specific points where delay is building, rather than assuming the site itself is the source of the issue. This will help distinguish operational bottlenecks from normal variation.

One limitation is that the dataset covers only one month and the appointment mix differs across sites. North has more specialist visits and a larger share of senior patients than Central, so the observed gap may reflect case mix and scheduling patterns as well as clinic operations. The data is therefore useful for comparison and prioritization, but it is not enough to assign cause.
"""
    (OUTPUT_DIR / "decision_note.md").write_text(note, encoding="utf-8")


def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    df = pd.read_csv(DATA_PATH)

    missing_values = df[["site", "wait_minutes"]].isna().sum()
    print("Row grain: one completed patient visit per site.")
    print("Missing values in analysis fields:")
    print(missing_values.to_string())

    summary = build_summary(df)
    summary.to_csv(OUTPUT_DIR / "site_wait_summary.csv", index=False)
    print("\nSite summary:")
    print(summary.to_string(index=False))

    build_chart(summary)
    write_decision_note()

    print("\nFiles created in output/:")
    for path in sorted(OUTPUT_DIR.iterdir()):
        print(path.name)


if __name__ == "__main__":
    main()
