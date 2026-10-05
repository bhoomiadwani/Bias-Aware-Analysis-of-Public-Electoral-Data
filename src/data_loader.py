from pathlib import Path
import pandas as pd

REQUIRED_COLUMNS = ["State", "Parliamentary Constituencies", "Voter Turnout Percent"]

def load_data(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")
    df = pd.read_csv(path)
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    print(f"Dataset shape: {df.shape}")
    print(df.head())
    return df
