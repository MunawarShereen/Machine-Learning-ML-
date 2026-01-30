import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import r2_score

# ==========================================
# 1. Load & Prepare Data
# ==========================================
data = load_diabetes()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

# ==========================================
# 2. Normal Linear Regression (No Penalty)
# ==========================================
lr = LinearRegression()
lr.fit(X_train, y_train)

y_pred_lr = lr.predict(X_test)

print("--- Linear Regression (Baseline) ---")
print("R2 Score:", r2_score(y_test, y_pred_lr))
print("Coefficients (Weights):\n", np.round(lr.coef_, 2))
print("-" * 50)

# ==========================================
# 3. Ridge Regression (L2 Regularization)
# ==========================================
# alpha is the same as Lambda in the formula
# alpha=0.1: Small penalty (Minor shrinking)
# alpha=100: Huge penalty (Weights become almost zero)

# Let's use alpha=0.1 (Standard usage)
r = Ridge(alpha=0.1)
r.fit(X_train, y_train)

y_pred_ridge = r.predict(X_test)

print("--- Ridge Regression (alpha=0.1) ---")
print("R2 Score:", r2_score(y_test, y_pred_ridge))
print("Coefficients (Weights):\n", np.round(r.coef_, 2))
print("-" * 50)

# ==========================================
# 4. Extreme Ridge (Your Request: alpha=100000)
# ==========================================
r_extreme = Ridge(alpha=100000)
r_extreme.fit(X_train, y_train)

print("--- Ridge Regression (alpha=100,000) ---")
# Notice how weights become 0.00
print("Coefficients (Weights):\n", np.round(r_extreme.coef_, 4)) 
print("Intercept:", r_extreme.intercept_)
