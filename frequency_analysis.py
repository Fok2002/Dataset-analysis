import pandas as pd

# Load the data
df = pd.read_csv('Autism_Screening_Data_Combined.csv')

# Function to create frequency and percentage table
def freq_percentage_table(column_name):
    freq = df[column_name].value_counts().sort_values(ascending=False)
    percentage = (freq / len(df) * 100).round(2)
    
    table = pd.DataFrame({
        'Frequency': freq,
        'Percentage': percentage
    })
    return table

# Analyze key columns
print("=" * 60)
print("FREQUENCY AND PERCENTAGE ANALYSIS")
print("=" * 60)

# 1. Gender Distribution
print("\n1. GENDER DISTRIBUTION")
print("-" * 60)
gender_table = freq_percentage_table('Sex')
gender_table.index = gender_table.index.map({'m': 'Male', 'f': 'Female'})
print(gender_table)
print(f"Total: {len(df)}")

# 2. Autism Screening Class
print("\n2. AUTISM SCREENING CLASS (Target Variable)")
print("-" * 60)
class_table = freq_percentage_table('Class')
print(class_table)

# 3. Age Distribution
print("\n3. AGE DISTRIBUTION")
print("-" * 60)
age_table = freq_percentage_table('Age')
print(age_table)

# 4. Jaundice
print("\n4. JAUNDICE HISTORY")
print("-" * 60)
jaundice_table = freq_percentage_table('Jauundice')
print(jaundice_table)

# 5. Family ASD History
print("\n5. FAMILY ASD HISTORY")
print("-" * 60)
family_table = freq_percentage_table('Family_ASD')
print(family_table)

print("\n" + "=" * 60)
