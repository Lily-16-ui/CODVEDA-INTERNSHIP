- README: Task 2 - Exploratory Data Analysis (Iris Dataset)
Project Overview: 
This project performs an Exploratory Data Analysis (EDA) on the classic Iris Dataset. The goal is to clean the data, calculate statistical trends, and visualize the relationships between different flower features (Sepal/Petal length and width).

1. Data Processing & Cleaning * Label Encoding: Converted categorical species names (setosa, versicolor, virginica) into numerical values (1, 2, 3). This allows for mathematical correlation analysis that isn't possible with text.

Path Handling: Implemented robust file pathing to handle Windows-specific directory structures.

2. Summary Statistics * Central Tendency: Calculated the Mean and Median for all features.

Distribution: Calculated Standard Deviation to understand data spread.

Frequency: Identified the Mode to see the most common measurements in the dataset.

3. Visualizations Created * Histogram: Used to visualize the distribution of Petal Length. It shows a clear "gap" between the small species (Setosa) and the larger ones.

Boxplot: Created to identify outliers in Sepal Width.

Scatter Plot: Plotted Petal Length vs. Petal Width to show the linear growth trend across species.

Correlation Heatmap: A color-coded matrix showing how features relate. (e.g., High correlation between Petal Length and Width).