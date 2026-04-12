# --- 1. THE TOOLS ---
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- 2. THE DATA ---
# Using the double backslash to keep your Windows path happy
df = pd.read_csv("C:\\Users\\JESULAYOMI\\PycharmProjects\\PythonProject1\\1) iris.csv")

# --- 3. THE "TRANSLATOR" (Label Encoding) ---
# This converts the text species into numbers so the computer can do math on them
species_translator = {
    'setosa': 1,
    'versicolor': 2,
    'virginica': 3
}
df['species_number'] = df['species'].map(species_translator)

# --- 4. THE MATH (Summary Statistics) ---
print("--- THE FIRST 5 ROWS (With Species Numbers) ---")
print(df.head())

print("\n--- SUMMARY STATISTICS (Mean, Median, Std Dev) ---")
print(df.describe())

print("\n--- MODE (Most Frequent Values) ---")
print(df.mode().iloc[0])

# --- 5. THE VISUALS ---

# A. Histogram: Seeing the "Shape" of the data
plt.figure(figsize=(8, 5))
sns.histplot(df['petal_length'], kde=True, color='blue')
plt.title("Distribution of Petal Length")
plt.show()

# B. Boxplot: Spotting the "Outliers"
plt.figure(figsize=(8, 5))
sns.boxplot(x='species', y='sepal_width', data=df)
plt.title("Sepal Width by Species (Check for Outliers)")
plt.show()

# C. Scatter Plot: Seeing the "Trend"
plt.figure(figsize=(8, 5))
sns.scatterplot(x='petal_length', y='petal_width', hue='species', data=df)
plt.title("Petal Length vs Petal Width")
plt.show()

# --- 6. THE RELATIONSHIPS (Correlation) ---
plt.figure(figsize=(10, 6))
# numeric_only=True ensures we only calculate correlation for the numbers
correlation_matrix = df.corr(numeric_only=True)
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap (Now including Species Number!)")
plt.show()

print("\nTask 2 Complete! All charts generated successfully.")