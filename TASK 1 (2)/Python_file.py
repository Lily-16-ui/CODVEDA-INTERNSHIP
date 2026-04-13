# Project: Task 1 - Data Cleaning and Preprocessing
# Author: TAIWO JESULAYOMI LYDIA
# Date: March 2026
# Description: This script cleans raw stock market data by handling missing values and standardizing formats.

import pandas as pd
import os

# ==========================================
# 1. SETUP: ENTER YOUR FILE NAME HERE
# ==========================================
INPUT_FILE = "C:\\Users\\JESULAYOMI\\PycharmProjects\PythonProject1\\2) Stock Prices Data Set.csv"
OUTPUT_FILE = "cleaned_dataset.csv"

if not os.path.exists(INPUT_FILE):
    print(f"Error: Could not find '{INPUT_FILE}'. check the name!")
else:
    df = pd.read_csv(INPUT_FILE)
    print("--- Original Data Preview ---")
    print(df.head())

    # ==========================================
    # 2. IDENTIFY & HANDLE MISSING VALUES
    # ==========================================
    print("\nMissing values before cleaning:")
    print(df.isnull().sum())

    # Option A: Impute (Fill) Numeric columns with the Mean
    num_cols = df.select_dtypes(include=['number']).columns
    df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

    # Option B: Remove rows where critical info is missing (e.g., if ID is null)
    # df.dropna(subset=['important_column_name'], inplace=True)

    # Option C: Fill Categorical/Text missing values with 'Unknown'
    obj_cols = df.select_dtypes(include=['object']).columns
    df[obj_cols] = df[obj_cols].fillna("Unknown")

    # ==========================================
    # 3. REMOVE DUPLICATE ROWS
    # ==========================================
    dupes = df.duplicated().sum()
    df.drop_duplicates(inplace=True)
    print(f"\nRemoved {dupes} duplicate rows.")

    # ==========================================
    # 4. STANDARDIZE DATA FORMATS
    # ==========================================

    # A. Standardize DATE formats
    # Finds any column with 'date' in the name and fixes it
    for col in df.columns:
        if 'date' in col.lower():
            df[col] = pd.to_datetime(df[col], errors='coerce')
            df[col] = df[col].dt.strftime('%Y-%m-%d')  # Format: 2024-12-31
            print(f"Standardized date column: {col}")

    # B. Standardize CATEGORICAL variables (Text)
    # Example: Making text Uppercase and removing accidental spaces
    for col in obj_cols:
        df[col] = df[col].astype(str).str.upper().str.strip()

    print("Standardized all text columns to UPPERCASE.")

    # ==========================================
    # 5. FINAL CHECK & SAVE
    # ==========================================
    print("\nMissing values after cleaning:")
    print(df.isnull().sum())

    df.to_csv(OUTPUT_FILE, index=False)
    print(f"\nSUCCESS: Cleaned data saved as '{OUTPUT_FILE}'")