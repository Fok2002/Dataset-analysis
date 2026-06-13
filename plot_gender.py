import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('Autism_Screening_Data_Combined.csv')

# Count the gender distribution
gender_counts = df['Sex'].value_counts()
gender_labels = ['Male', 'Female']
gender_data = [gender_counts['m'], gender_counts['f']]
percentages = (gender_counts / len(df) * 100).round(2)

# Create figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Bar chart
colors = ['#3498db', '#e74c3c']
bars = ax1.bar(gender_labels, gender_data, color=colors, alpha=0.7, edgecolor='black', linewidth=1.5)
ax1.set_ylabel('Count', fontsize=12, fontweight='bold')
ax1.set_title('Gender Distribution - Count', fontsize=14, fontweight='bold')
ax1.grid(axis='y', alpha=0.3)

# Add count labels on bars
for bar, count in zip(bars, gender_data):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height,
            f'{int(count)}',
            ha='center', va='bottom', fontsize=11, fontweight='bold')

# Pie chart
wedges, texts, autotexts = ax2.pie(gender_data, labels=gender_labels, autopct='%1.2f%%',
                                     colors=colors, startangle=90, textprops={'fontsize': 11})
ax2.set_title('Gender Distribution - Percentage', fontsize=14, fontweight='bold')

# Make percentage text bold
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(12)

plt.suptitle('Autism Screening Data - Gender Analysis', fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('gender_distribution.png', dpi=300, bbox_inches='tight')
print("Graph saved as 'gender_distribution.png'")
plt.show()
