from pathlib import Path

def generate_report(df, stats, quality, path: Path):
    text = f"""BIAS-AWARE ELECTORAL DATA ANALYSIS

Descriptive findings
States/UTs analyzed: {len(df)}
Mean voter turnout: {stats["mean_turnout"]:.2f}%
Highest turnout: {stats["highest_state"]} ({stats["highest_turnout"]:.2f}%)
Lowest turnout: {stats["lowest_state"]} ({stats["lowest_turnout"]:.2f}%)

Data quality
Missing values before cleaning: {quality["missing_values_before"]}
Duplicate rows before cleaning: {quality["duplicates_before"]}
Rows removed during cleaning: {quality["rows_removed"]}

Turnout groups
{stats["group_counts"]}

Bias-aware interpretation
The results describe observed differences in aggregated State/UT-level turnout.
Turnout differences alone are not evidence of electoral bias, manipulation, or
unfairness. Geographic, social, demographic, administrative and accessibility
factors are not fully represented in this simple dataset.

Limitations
- Aggregated public data are used instead of individual voter records.
- State/UT aggregation can hide constituency or demographic differences.
- Source-data quality and representation limitations may affect results.
- Stronger conclusions require contextual variables and suitable statistical tests.
"""
    path.write_text(text, encoding="utf-8")
