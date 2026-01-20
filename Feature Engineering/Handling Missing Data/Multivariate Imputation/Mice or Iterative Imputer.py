import pandas as pd
import numpy as np
from sklearn.experimental import enable_iterative_imputer  # <--- MUST IMPORT THIS
from sklearn.impute import IterativeImputer
from sklearn.linear_model import LinearRegression

# ==========================================
# 1. Create Dummy Data (Multivariate)
# ==========================================
data = {
    'Age': [25, 30, np.nan, 22, 28, np.nan, 35],
    'Salary': [50000, 60000, 55000, np.nan, 62000, 58000, 70000],
    'Tax': [2000, 2500, np.nan, 1500, np.nan, 2300, 3000]
}
df = pd.DataFrame(data)

print("Original Data (With Missing Values):")
print(df)
print("-" * 30)

# ==========================================
# 2. Apply MICE (Iterative Imputer)
# ==========================================

# estimator: Which model to use for prediction? (LinearRegression is standard)
# max_iter: How many times to repeat the cycle? (usually 10 is enough)
# tol: Tolerance (Stop if difference is smaller than this number)
lr = LinearRegression()
mice_imputer = IterativeImputer(estimator=lr, max_iter=10, tol=1e-3, random_state=0)

# fit_transform returns a 2D Numpy Array
mice_data_array = mice_imputer.fit_transform(df)

# Convert back to DataFrame
df_mice = pd.DataFrame(mice_data_array, columns=df.columns)

print("Data After MICE Imputation:")
print(np.round(df_mice, 2))
