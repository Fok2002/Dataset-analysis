import pandas as pd

# Load the data
df = pd.read_csv('Autism_Screening_Data_Combined.csv')

# Count the gender distribution
gender_counts = df['Sex'].value_counts()
gender_percentages = (gender_counts / len(df) * 100).round(2)

# Create a summary table
summary = pd.DataFrame({
    'Count': gender_counts,
    'Percentage': gender_percentages
})

# Rename index for clarity
summary.index.name = 'Gender'
summary = summary.rename(index={'m': 'Male', 'f': 'Female'})

# Display results
print("=" * 50)
print("GENDER DISTRIBUTION ANALYSIS")
print("=" * 50)
print(summary)
print("=" * 50)
print(f"Total Records: {len(df)}")
print("=" * 50)
