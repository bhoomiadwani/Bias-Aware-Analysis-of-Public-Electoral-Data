from pathlib import Path
import pandas as pd

REQUIRED_COLUMNS = ["State", "Parliamentary Constituencies", "Voter Turnout Percent"]

COLUMN_ALIASES = {
    "Parliamentary_Constituencies": "Parliamentary Constituencies",
    "Voter_Turnout_Percent": "Voter Turnout Percent",
}

def load_data(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    df = pd.read_csv(path)
    df.columns = [str(c).strip() for c in df.columns]

    # Accept both the project-standard column names and the underscore
    # versions commonly found in CSV datasets.
    df = df.rename(columns=COLUMN_ALIASES)

    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    print(f"Dataset shape: {df.shape}")
    print(df.head())
    return df
