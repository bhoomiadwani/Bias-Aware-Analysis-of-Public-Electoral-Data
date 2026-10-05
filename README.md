# Bias-Aware Analysis of Public Electoral Data

A Python academic data-analysis project for cleaning, analyzing and visualizing aggregated voter turnout across Indian States and Union Territories.

## Features
- Public electoral CSV import and validation
- Missing-value and duplicate checks
- Numeric cleaning and State/UT name cleaning
- Mean turnout and turnout gap from the mean
- Low, Moderate, High and Very High turnout groups
- Six required visualizations
- Bias-aware findings and limitations
- Optional Streamlit dashboard

## Structure
data/raw contains the input dataset.
data/processed contains cleaned output.
outputs/graphs contains six generated charts.
outputs/report contains the findings report.
src contains the analysis modules.
dashboard contains the optional Streamlit interface.
main.py runs the complete pipeline.

## Setup
pip install -r requirements.txt

Place electoral_data.csv in data/raw and run:
python main.py

Optional dashboard:
streamlit run dashboard/app.py

## Required columns
State
Parliamentary Constituencies
Voter Turnout Percent

## Turnout groups
Low: below 60%
Moderate: 60% to below 70%
High: 70% to 80%
Very High: above 80%

## Required visualizations
1. All States/UTs turnout
2. Top 10 turnout
3. Bottom 10 turnout
4. Turnout distribution
5. Parliamentary constituencies vs turnout
6. Turnout-group summary

## Bias-aware interpretation
This project is descriptive. Turnout differences are patterns requiring context and should not be treated as proof of electoral unfairness. Aggregated State/UT data can hide local and demographic differences.
