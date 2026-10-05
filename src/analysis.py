import numpy as np

def analyze_data(df):
    data = df.copy()
    mean_turnout = float(data["Voter Turnout Percent"].mean())
    data["Turnout_Gap_From_Mean"] = (data["Voter Turnout Percent"] - mean_turnout).round(2)
    conditions = [
        data["Voter Turnout Percent"] < 60,
        data["Voter Turnout Percent"].between(60, 69.999999),
        data["Voter Turnout Percent"].between(70, 80),
        data["Voter Turnout Percent"] > 80,
    ]
    data["Turnout_Group"] = np.select(
        conditions, ["Low", "Moderate", "High", "Very High"], default="Unclassified"
    )
    stats = {
        "mean_turnout": mean_turnout,
        "highest_state": data.loc[data["Voter Turnout Percent"].idxmax(), "State"],
        "highest_turnout": float(data["Voter Turnout Percent"].max()),
        "lowest_state": data.loc[data["Voter Turnout Percent"].idxmin(), "State"],
        "lowest_turnout": float(data["Voter Turnout Percent"].min()),
        "group_counts": data["Turnout_Group"].value_counts().to_dict(),
    }
    return data, stats
