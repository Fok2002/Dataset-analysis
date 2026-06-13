# Dataset-analysis

```markdown
 Autism Screening Data Analysis

 Overview

This project analyzes an autism screening dataset to explore gender distribution, frequency statistics, and visual gender comparisons. It includes three Python scripts that load the dataset and produce summary tables and a saved chart.

 Files

- `Autism_Screening_Data_Combined.csv` - Dataset used for analysis
- `analyze_gender.py` - Computes gender distribution counts and percentages
- `frequency_analysis.py` - Generates frequency and percentage tables for selected dataset features
- `plot_gender.py` - Creates and saves a bar + pie chart for gender distribution
- `README.md` - Project documentation

 Requirements

- Python 3.x
- `pandas`
- `matplotlib`

Install dependencies with:

```bash
pip install pandas matplotlib
```

 Usage

Run the analysis scripts from the repository folder:

```bash
python analyze_gender.py
python frequency_analysis.py
python plot_gender.py
```

plot_gender.py saves the visualization as:

- gender_distribution.png

 What Each Script Does

- analyze_gender.py
  - Loads the dataset
  - Counts male and female records
  - Displays a summary table with counts and percentages

- frequency_analysis.py
  - Loads the dataset
  - Builds frequency and percentage tables for:
    - `Sex`
    - `Class`
    - `Age`
    - `Jaundice`
    - `Family_ASD`

- plot_gender.py
  - Loads the dataset
  - Draws a bar chart and pie chart for gender distribution
  - Saves the chart image file

Data Fields Used

- `Sex` — Gender value (`m` or `f`)
- `Class` — Autism screening class / target variable
- `Age` — Age values by record
- `Jaundice` — History of jaundice
- `Family_ASD` — Family history of autism spectrum disorder

 Notes

- Ensure Autism_Screening_Data_Combined.csv is in the same folder as the scripts.
- The charts and analysis are designed for quick exploratory data review.
- You can extend the project by adding more visualizations or statistical summaries.
```
