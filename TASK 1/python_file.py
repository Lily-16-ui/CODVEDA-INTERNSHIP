import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Define full, descriptive names for all columns
full_names = [
    'Crime_Rate', 'Residential_Zone', 'Business_Acres', 'Charles_River',
    'Nitric_Oxide', 'Avg_Rooms', 'Age_of_Home', 'Distance_to_Employment',
    'Highway_Accessibility', 'Property_Tax', 'Pupil_Teacher_Ratio',
    'Population_Index', 'Lower_Status_Percent', 'House_Price'
]

# 2. Load the raw file
# We use sep='\s+' because the file is separated by spaces, not commas
df = pd.read_csv('4) house Prediction Data Set.csv', sep='\s+', names=full_names)

# 3. Save the new "Cleaned" version with descriptive headers
# This file is perfect for your final submission
df.to_csv('house_data_descriptive.csv', index=False)
print("Step 1: Cleaned descriptive dataset saved as 'house_data_descriptive.csv'")

# 4. Prepare data for Linear Regression
# X (Predictor): Average number of rooms
# y (Target): Median House Price
X = df[['Avg_Rooms']]
y = df['House_Price']

# 5. Split the data (80% Training to learn patterns, 20% Testing to evaluate)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. Initialize and "Fit" the Model (Training)
model = LinearRegression()
model.fit(X_train, y_train)

# 7. Make Predictions using the test set
y_pred = model.predict(X_test)

# 8. Evaluate the Model (The "Report Card")
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
coefficient = model.coef_[0]

print("\n--- REGRESSION ANALYSIS RESULTS ---")
print(f"R-squared Score: {r2:.4f}")
print(f"Mean Squared Error: {mse:.4f}")
print(f"Coefficient (Increase per room): {coefficient:.4f}")
print("-----------------------------------\n")

# 9. Create the Scatter Plot
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='teal', alpha=0.6, label='Actual House Prices')
plt.plot(X_test, y_pred, color='orange', linewidth=3, label='Regression Line (Prediction)')

# Labels and Styling
plt.xlabel('Average Number of Rooms')
plt.ylabel('House Price (in $1,000s)')
plt.title('Task 1: Predicting House Price based on Average Rooms')
plt.legend()
plt.grid(True)

# 10. Save and Show the Result
plt.savefig('house_price_analysis_plot.png')
print("Step 2: Analysis plot saved as 'house_price_analysis_plot.png'")
plt.show()