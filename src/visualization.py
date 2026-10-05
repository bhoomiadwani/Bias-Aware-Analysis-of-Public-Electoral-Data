from pathlib import Path
import matplotlib.pyplot as plt

def _save(fig, path):
    fig.tight_layout()
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)

def generate_all_visualizations(df, mean_turnout, output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
    ordered = df.sort_values("Voter Turnout Percent")
    fig, ax = plt.subplots(figsize=(11, 9))
    ax.barh(ordered["State"], ordered["Voter Turnout Percent"])
    ax.axvline(mean_turnout, linestyle="--", label=f"Mean {mean_turnout:.2f}%")
    ax.set_title("All States/UTs: Voter Turnout")
    ax.set_xlabel("Voter Turnout (%)")
    ax.set_ylabel("State / UT")
    ax.legend()
    _save(fig, output_dir / "all_states_turnout.png")

    for ascending, filename, title in [
        (False, "top10_turnout.png", "Top 10 States/UTs by Turnout"),
        (True, "bottom10_turnout.png", "Bottom 10 States/UTs by Turnout"),
    ]:
        subset = df.sort_values("Voter Turnout Percent", ascending=ascending).head(10)
        subset = subset.sort_values("Voter Turnout Percent")
        fig, ax = plt.subplots(figsize=(9, 6))
        ax.barh(subset["State"], subset["Voter Turnout Percent"])
        ax.set_title(title)
        ax.set_xlabel("Voter Turnout (%)")
        ax.set_ylabel("State / UT")
        _save(fig, output_dir / filename)

    fig, ax = plt.subplots(figsize=(9, 6))
    ax.hist(df["Voter Turnout Percent"], bins=10, edgecolor="black")
    ax.set_title("Distribution of Voter Turnout")
    ax.set_xlabel("Voter Turnout (%)")
    ax.set_ylabel("Number of States/UTs")
    _save(fig, output_dir / "turnout_distribution.png")

    fig, ax = plt.subplots(figsize=(9, 6))
    ax.scatter(df["Parliamentary Constituencies"], df["Voter Turnout Percent"], alpha=0.75)
    ax.set_title("Parliamentary Constituencies vs Voter Turnout")
    ax.set_xlabel("Number of Parliamentary Constituencies")
    ax.set_ylabel("Voter Turnout (%)")
    _save(fig, output_dir / "constituency_vs_turnout.png")

    order = ["Low", "Moderate", "High", "Very High"]
    counts = df["Turnout_Group"].value_counts().reindex(order, fill_value=0)
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(counts.index, counts.values)
    ax.set_title("Turnout Group Summary")
    ax.set_xlabel("Turnout Group")
    ax.set_ylabel("Number of States/UTs")
    _save(fig, output_dir / "turnout_groups.png")
