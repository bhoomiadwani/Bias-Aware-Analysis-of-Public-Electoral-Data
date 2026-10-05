import pandas as pd

def clean_data(df):
    data = df.copy()
    data.columns = [str(c).strip() for c in data.columns]
    missing_before = int(data.isna().sum().sum())
    duplicates_before = int(data.duplicated().sum())
    data["State"] = data["State"].astype("string").str.strip()
    data["Parliamentary Constituencies"] = pd.to_numeric(data["Parliamentary Constituencies"], errors="coerce")
    data["Voter Turnout Percent"] = pd.to_numeric(
        data["Voter Turnout Percent"].astype("string").str.replace("%", "", regex=False).str.strip(),
        errors="coerce"
    )
    data = data.drop_duplicates()
    data = data.dropna(subset=["State", "Parliamentary Constituencies", "Voter Turnout Percent"])
    quality = {
        "missing_values_before": missing_before,
        "duplicates_before": duplicates_before,
        "rows_removed": len(df) - len(data),
    }
    return data.reset_index(drop=True), quality
