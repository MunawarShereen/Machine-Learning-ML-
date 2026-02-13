import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

# ==========================================
# 1. Load Data & Select One Feature
# ==========================================
# We use only the 3rd column (BMI) to visualize 2D plot
data = load_diabetes()
X = data.data[:, 2].reshape(-1, 1) 
y = data.target

# Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ==========================================
# 2. Linear Regression (Degree 1) - For Comparison
# ==========================================
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)

# ==========================================
# 3. Polynomial Regression (Degree 3)
# ==========================================
# Step A: Transform the features (x -> x, x^2, x^3)
poly = PolynomialFeatures(degree=3)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

# Step B: Train Linear Regression on the new Polynomial features
poly_reg = LinearRegression()
poly_reg.fit(X_train_poly, y_train)

# ==========================================
# 4. Evaluation
# ==========================================
y_pred_lin = lin_reg.predict(X_test)
y_pred_poly = poly_reg.predict(X_test_poly)

print(f"Linear Regression R2: {r2_score(y_test, y_pred_lin):.4f}")
print(f"Polynomial Regression (Degree 3) R2: {r2_score(y_test, y_pred_poly):.4f}")
print("-" * 30)

# ==========================================
# 5. Visualization
# ==========================================
plt.figure(figsize=(10, 6))

# Plot actual data points
plt.scatter(X_test, y_test, color='black', label='Actual Data')

# Plot Linear Regression Line (Red)
plt.plot(X_test, y_pred_lin, color='red', linewidth=2, label='Linear (Degree 1)')

# Plot Polynomial Regression Curve (Blue)
# NOTE: To plot a curve properly, we must sort the X values, otherwise the line will be messy
sorted_zip = sorted(zip(X_test, y_pred_poly))
X_test_sorted, y_poly_sorted = zip(*sorted_zip)

plt.plot(X_test_sorted, y_poly_sorted, color='blue', linewidth=3, label='Polynomial (Degree 3)')

plt.title("Linear vs Polynomial Regression")
plt.xlabel("BMI (Normalized)")
plt.ylabel("Diabetes Progression")
plt.legend()
plt.show()
