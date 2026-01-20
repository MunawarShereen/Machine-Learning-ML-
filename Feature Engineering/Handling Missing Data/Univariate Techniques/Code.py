import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer, MissingIndicator

# ==========================================
# 1. Create Dummy Data
# ==========================================
data = {
    'Age': [25, 30, np.nan, 22, 28, np.nan, 35, 40, np.nan, 29], 
    'Salary': [50000, 60000, 55000, np.nan, 62000, 58000, np.nan, 70000, 51000, 65000],
    'City': ['Lahore', 'Karachi', np.nan, 'Lahore', 'Islamabad', 'Karachi', np.nan, 'Lahore', 'Quetta', 'Lahore']
}
df = pd.DataFrame(data)

print("Original Data:")
print(df)
print("-" * 30)

# ==========================================
# 2. Numerical Techniques (Sklearn)
# ==========================================

# --- A. Mean/Median Imputation ---

# 1. Mean Strategy
imputer_mean = SimpleImputer(strategy='mean')
# Note: Sklearn requires 2D array, so use double brackets [['Salary']]
df['Salary_Mean'] = imputer_mean.fit_transform(df[['Salary']])

# 2. Median Strategy
imputer_median = SimpleImputer(strategy='median')
df['Age_Median'] = imputer_median.fit_transform(df[['Age']])


# --- B. Arbitrary Value Imputation ---
# We use strategy='constant' and define the fill_value
imputer_arbitrary = SimpleImputer(strategy='constant', fill_value=99)
df['Age_Arbitrary'] = imputer_arbitrary.fit_transform(df[['Age']])


# --- C. End of Distribution Imputation ---
# Sklearn doesn't calculate "End of Dist" automatically. 
# We calculate the value first, then use 'constant' strategy.
# Calculation: Mean + 3 * Sigma
eod_value = df['Age'].mean() + (3 * df['Age'].std())

imputer_eod = SimpleImputer(strategy='constant', fill_value=eod_value)
df['Age_End_Dist'] = imputer_eod.fit_transform(df[['Age']])


# --- D. Missing Indicator ---
# Sklearn has a specific class for this
indicator = MissingIndicator(features='all') # features='all' marks all columns provided
# This returns a boolean (True/False) matrix
missing_indicators = indicator.fit_transform(df[['Age']])
# Convert to integer (0/1) for better visibility
df['Age_Is_Missing'] = missing_indicators.astype(int)


# --- NOTE ON RANDOM SAMPLE ---
# Sklearn does NOT have a built-in 'Random Sample' imputer. 
# For Random Sample, we stick to the Pandas method you used previously.


print("Numerical Imputation Results (Sklearn):")
print(df[['Age', 'Age_Median', 'Salary_Mean', 'Age_Arbitrary', 'Age_End_Dist', 'Age_Is_Missing']])
print("-" * 30)


# ==========================================
# 3. Categorical Techniques (Sklearn)
# ==========================================

# --- A. Most Frequent (Mode) ---
# strategy='most_frequent' works for text/categories
imputer_mode = SimpleImputer(strategy='most_frequent')
df['City_Mode'] = imputer_mode.fit_transform(df[['City']])


# --- B. New Category Imputation ---
# We use 'constant' strategy and set fill_value to our new category name
imputer_new_cat = SimpleImputer(strategy='constant', fill_value='Missing')
df['City_New_Cat'] = imputer_new_cat.fit_transform(df[['City']])


print("Categorical Imputation Results (Sklearn):")
print(df[['City', 'City_Mode', 'City_New_Cat']])
