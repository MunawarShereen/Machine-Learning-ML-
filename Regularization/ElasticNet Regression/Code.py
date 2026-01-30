import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# ==========================================
# 1. Load & Split Data
# ==========================================
X, y = load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

print("--- Comparison of Models ---")

# ==========================================
# 2. Simple Linear Regression (Baseline)
# ==========================================
reg = LinearRegression()
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)
print(f"Linear Regression R2: {r2_score(y_test, y_pred):.4f}")

# ==========================================
# 3. Ridge Regression (L2)
# ==========================================
# Keeps all features, just shrinks weights
ridge = Ridge(alpha=0.1)
ridge.fit(X_train, y_train)
y_pred_ridge = ridge.predict(X_test)
print(f"Ridge (alpha=0.1) R2: {r2_score(y_test, y_pred_ridge):.4f}")

# ==========================================
# 4. Lasso Regression (L1)
# ==========================================
# Removes features (Feature Selection)
lasso = Lasso(alpha=0.01)
lasso.fit(X_train, y_train)
y_pred_lasso = lasso.predict(X_test)
print(f"Lasso (alpha=0.01) R2: {r2_score(y_test, y_pred_lasso):.4f}")

# ==========================================
# 5. ElasticNet (Combination)
# ==========================================
# alpha = Total penalty strength
# l1_ratio = How much Lasso to mix in? (0.9 means 90% Lasso, 10% Ridge)
en = ElasticNet(alpha=0.005, l1_ratio=0.9)
en.fit(X_train, y_train)
y_pred_en = en.predict(X_test)
print(f"ElasticNet (alpha=0.005, l1_ratio=0.9) R2: {r2_score(y_test, y_pred_en):.4f}")
