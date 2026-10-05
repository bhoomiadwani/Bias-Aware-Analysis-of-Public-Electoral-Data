from pathlib import Path
import sys
import tempfile
import streamlit as st
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.data_cleaning import clean_data
from src.analysis import analyze_data
from src.visualization import generate_all_visualizations

st.set_page_config(page_title="Bias-Aware Electoral Analysis", layout="wide")
st.title("Bias-Aware Analysis of Public Electoral Data")
st.caption("Descriptive analysis of aggregated State/UT-level voter turnout.")

uploaded = st.file_uploader("Upload electoral CSV", type=["csv"])

if uploaded:
    raw = pd.read_csv(uploaded)

    # Accept both the project-standard names and underscore-style CSV names.
    raw.columns = [str(c).strip() for c in raw.columns]
    raw = raw.rename(columns={
        "Parliamentary_Constituencies": "Parliamentary Constituencies",
        "Voter_Turnout_Percent": "Voter Turnout Percent",
    })

    st.subheader("Data Preview")
    st.dataframe(raw.head(10), use_container_width=True)

    try:
        cleaned, quality = clean_data(raw)
        analyzed, stats = analyze_data(cleaned)

        c1, c2, c3 = st.columns(3)
        c1.metric("States/UTs analyzed", len(analyzed))
        c2.metric("Mean turnout", f"{stats['mean_turnout']:.2f}%")
        c3.metric("Rows removed", quality["rows_removed"])

        st.subheader("Analyzed Data")
        st.dataframe(analyzed, use_container_width=True)

        with tempfile.TemporaryDirectory() as tmp:
            generate_all_visualizations(
                analyzed,
                stats["mean_turnout"],
                Path(tmp)
            )

            st.subheader("Visualizations")
            for filename in [
                "all_states_turnout.png",
                "top10_turnout.png",
                "bottom10_turnout.png",
                "turnout_distribution.png",
                "constituency_vs_turnout.png",
                "turnout_groups.png",
            ]:
                st.image(
                    str(Path(tmp) / filename),
                    caption=filename.replace("_", " ").title()
                )

        st.warning(
            "Bias-aware note: turnout differences are descriptive patterns, "
            "not proof of electoral unfairness."
        )

    except Exception as exc:
        st.error(str(exc))
else:
    st.info(
        "Upload a CSV containing State, Parliamentary Constituencies, "
        "and Voter Turnout Percent."
    )
