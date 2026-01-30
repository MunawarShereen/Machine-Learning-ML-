import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import Lasso, LinearRegression
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

# ==========================================
# 1. Create Synthetic Data
# ==========================================
X, y = make_regression(n_samples=100, n_features=1, n_informative=1, n_targets=1, noise=20, random_state=13)

# ==========================================
# 2. Split Data
# ==========================================
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

# ==========================================
# 3. Visualize Data
# ==========================================
plt.scatter(X, y, color='blue', label='Data Points')
plt.title("Synthetic Data Regression")
plt.xlabel("Input X")
plt.ylabel("Output y")
plt.show()

# ==========================================
# 4. Standard Linear Regression (No Penalty)
# ==========================================
reg = LinearRegression()
reg.fit(X_train, y_train)

print("--- Linear Regression ---")
print("Coefficient (m):", reg.coef_)
print("Intercept (b):", reg.intercept_)
print("-" * 30)

# ==========================================
# 5. Lasso Regression (L1 Penalty)
# ==========================================
# Alpha = Lambda (Penalty Strength)
# Case A: Small Alpha (0.1) -> Minimal shrinking
lasso_small = Lasso(alpha=0.1)
lasso_small.fit(X_train, y_train)

print("--- Lasso Regression (alpha=0.1) ---")
print("Coefficient (m):", lasso_small.coef_)
print("Intercept (b):", lasso_small.intercept_)
print("-" * 30)

# Case B: Large Alpha (10) -> Strong shrinking
lasso_large = Lasso(alpha=10)
lasso_large.fit(X_train, y_train)

print("--- Lasso Regression (alpha=10) ---")
print("Coefficient (m):", lasso_large.coef_)
print("Intercept (b):", lasso_large.intercept_)

# ==========================================
# 6. Visual Comparison (Best Fit Lines)
# ==========================================
plt.scatter(X, y, color='blue', alpha=0.5)
# Plot Linear Regression Line (Red)
plt.plot(X, reg.predict(X), color='red', label='Linear Regression')
# Plot Lasso Line (Green) - Notice it might be slightly different
plt.plot(X, lasso_large.predict(X), color='green', label='Lasso (alpha=10)')
plt.legend()
plt.title("Linear Regression vs Lasso")
plt.show()
