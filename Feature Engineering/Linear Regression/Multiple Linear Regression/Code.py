import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# ==========================================
# 1. Create Sample Data (House Price)
# ==========================================
data = {
    'Size_sqft': [1000, 1500, 2000, 2500, 3000],   # Input 1
    'Rooms':     [2, 3, 3, 4, 5],                  # Input 2
    'Age_yrs':   [10, 5, 15, 2, 1],                # Input 3
    'Price':     [50, 75, 80, 120, 150]            # Output (Target)
}
df = pd.DataFrame(data)

print("Data:")
print(df)
print("-" * 30)

# ==========================================
# 2. Split Input (X) and Output (y)
# ==========================================
# X now has 3 columns (Size, Rooms, Age)
X = df[['Size_sqft', 'Rooms', 'Age_yrs']]
y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ==========================================
# 3. Train Model
# ==========================================
lr = LinearRegression()
lr.fit(X_train, y_train)

# ==========================================
# 4. Check Coefficients (Weights)
# ==========================================
print("Intercept (Beta 0):", lr.intercept_)
print("Coefficients (Beta 1, Beta 2, Beta 3):", lr.coef_)

# Interpretation:
# The model found 3 weights corresponding to Size, Rooms, and Age.
