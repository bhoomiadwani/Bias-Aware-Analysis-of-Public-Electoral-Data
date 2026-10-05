from pathlib import Path
from src.data_loader import load_data
from src.data_cleaning import clean_data
from src.analysis import analyze_data
from src.visualization import generate_all_visualizations
from src.bias_report import generate_report
from src.export import export_cleaned_data

BASE = Path(__file__).resolve().parent
INPUT = BASE / "data" / "raw" / "electoral_data.csv"
PROCESSED = BASE / "data" / "processed"
GRAPHS = BASE / "outputs" / "graphs"
REPORT = BASE / "outputs" / "report" / "findings.txt"

def main():
    PROCESSED.mkdir(parents=True, exist_ok=True)
    GRAPHS.mkdir(parents=True, exist_ok=True)
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    print("=== Bias-Aware Analysis of Public Electoral Data ===")
    df = load_data(INPUT)
    cleaned, quality = clean_data(df)
    analyzed, stats = analyze_data(cleaned)
    export_cleaned_data(analyzed, PROCESSED / "cleaned_data.csv")
    generate_all_visualizations(analyzed, stats["mean_turnout"], GRAPHS)
    generate_report(analyzed, stats, quality, REPORT)
    print(f"Rows analyzed: {len(analyzed)}")
    print(f"Mean turnout: {stats['mean_turnout']:.2f}%")

if __name__ == "__main__":
    main()
