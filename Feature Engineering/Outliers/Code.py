import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ==========================================
# 0. Create Custom Data (Synthetic)
# ==========================================
np.random.seed(42)

# 1. CGPA: Normal Distribution (Mean=7, Std=1)
# 1000 students
cgpa = np.random.normal(7, 1, 1000)
# Add 5 artificial outliers (extremely high and low values)
cgpa = np.append(cgpa, [15, 14, 13, -2, -5]) 

# 2. Placement Marks: Skewed Distribution
# Log-normal distribution is naturally skewed (Right Skewed)
marks = np.random.lognormal(3, 1, 1000)
# Add 5 artificial outliers to match the length of CGPA (1005 rows total)
marks = np.append(marks, [1000, 1100, 1200, 1300, 1400])

# Create DataFrame
df = pd.DataFrame({'cgpa': cgpa, 'placement_exam_marks': marks})

print("Original Data Description:")
print(df.describe())
print("-" * 30)

# ==========================================
# Method 1: Z-Score Method
# (Best for Normal Distributions like CGPA)
# ==========================================
print("\n--- Method 1: Z-Score Method (on CGPA) ---")

# 1. Visualization
sns.displot(df['cgpa'], kde=True)
plt.title("CGPA Distribution (Before)")
plt.show()

# 2. Calculate Z-Score
# Formula: (x - mean) / std
df['cgpa_zscore'] = (df['cgpa'] - df['cgpa'].mean()) / df['cgpa'].std()

# 3. Define Limits (Mean +/- 3*Std)
upper_limit_z = df['cgpa'].mean() + 3 * df['cgpa'].std()
lower_limit_z = df['cgpa'].mean() - 3 * df['cgpa'].std()

print(f"Z-Score Upper Limit: {upper_limit_z:.2f}")
print(f"Z-Score Lower Limit: {lower_limit_z:.2f}")

# 4. Trimming (Removing rows)
# Keep only data between -3 and +3 Z-score
new_df_z = df[(df['cgpa_zscore'] < 3) & (df['cgpa_zscore'] > -3)]

# 5. Capping (Winsorization)
# Replace outliers with the limits
df['cgpa_capped_z'] = np.where(
    df['cgpa'] > upper_limit_z,
    upper_limit_z,
    np.where(
        df['cgpa'] < lower_limit_z,
        lower_limit_z,
        df['cgpa']
    )
)

# ==========================================
# Method 2: IQR Method
# (Best for Skewed Distributions like Marks)
# ==========================================
print("\n--- Method 2: IQR Method (on Placement Marks) ---")

# 1. Visualization
sns.displot(df['placement_exam_marks'], kde=True)
plt.title("Marks Distribution (Before)")
plt.show()

# 2. Calculate Q1, Q3, IQR
Q1 = df['placement_exam_marks'].quantile(0.25)
Q3 = df['placement_exam_marks'].quantile(0.75)
IQR = Q3 - Q1

# 3. Define Limits (1.5 * IQR rule)
upper_limit_iqr = Q3 + 1.5 * IQR
lower_limit_iqr = Q1 - 1.5 * IQR

print(f"IQR Upper Limit: {upper_limit_iqr:.2f}")
print(f"IQR Lower Limit: {lower_limit_iqr:.2f}")

# 4. Trimming
new_df_iqr = df[(df['placement_exam_marks'] <= upper_limit_iqr) & (df['placement_exam_marks'] >= lower_limit_iqr)]

# 5. Capping
df['marks_capped_iqr'] = np.where(
    df['placement_exam_marks'] > upper_limit_iqr,
    upper_limit_iqr,
    np.where(
        df['placement_exam_marks'] < lower_limit_iqr,
        lower_limit_iqr,
        df['placement_exam_marks']
    )
)

# ==========================================
# Method 3: Percentile Method
# (Useful when you want to filter top/bottom 1%)
# ==========================================
print("\n--- Method 3: Percentile Method (on Placement Marks) ---")

# 1. Define Limits (e.g., 1st and 99th percentile)
upper_limit_p = df['placement_exam_marks'].quantile(0.99)
lower_limit_p = df['placement_exam_marks'].quantile(0.01)

print(f"Percentile Upper Limit (99th): {upper_limit_p:.2f}")
print(f"Percentile Lower Limit (1st): {lower_limit_p:.2f}")

# 2. Trimming
new_df_p = df[(df['placement_exam_marks'] <= upper_limit_p) & (df['placement_exam_marks'] >= lower_limit_p)]

# 3. Capping
df['marks_capped_percentile'] = np.where(
    df['placement_exam_marks'] > upper_limit_p,
    upper_limit_p,
    np.where(
        df['placement_exam_marks'] < lower_limit_p,
        lower_limit_p,
        df['placement_exam_marks']
    )
)

print("-" * 30)
print("Data Handling Complete. Columns added for comparison.")
print(df.columns)
