# Task 1: Data Cleaning and Preprocessing
## Project Overview
This project focuses on taking a raw financial dataset containing stock prices and transforming it into a clean, "analysis-ready" format. The process involves handling missing values, removing duplicates, and ensuring consistent data formatting.

## The Cleaning Process
1. Data Loading
Library: Used pandas for robust data manipulation.

Action: Loaded the raw CSV file into a DataFrame.

2. Identifying Missing Data
Method: Used .isnull().sum() to pinpoint exactly which columns had gaps.

Findings: Identified missing entries in the open, high, and low price columns.

3. Handling Missing Values (Imputation)
Strategy: Applied Mean Imputation.

Logic: Rather than deleting rows (which loses valuable data), missing numeric values were filled with the average of that specific column to maintain the dataset's statistical integrity.

4. Removing Duplicates
Action: Scanned the entire dataset for identical rows.

Result: Ensured that every data point represents a unique market entry, preventing skewed results in future analysis.

5. Standardizing Data Formats
Date Standardization: Converted various date strings into a uniform YYYY-MM-DD format using pd.to_datetime.

Text Cleaning: Standardized the symbol column by removing whitespace and converting all tickers to UPPERCASE for consistent grouping.

6. Verification & Export
Final Check: Re-ran the missing value check to confirm a "Zero-Null" status.

Output: Saved the finalized data as cleaned_dataset.csv.

## Final Results
Initial Issues: Missing price data and inconsistent text/date casing.

Final State: 100% complete dataset with standardized columns, ready for visualization or modeling.
