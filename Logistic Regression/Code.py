import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# ==========================================
# 1. Load Dataset
# ==========================================
# This dataset has 30 features and a binary target (0 = Malignant, 1 = Benign)
data = load_breast_cancer()
X = data.data
y = data.target

print(f"Dataset Loaded. Features: {X.shape[1]}, Samples: {X.shape[0]}")
print("Target Classes:", data.target_names)  # ['malignant', 'benign']
print("-" * 30)

# ==========================================
# 2. Split Data (Train/Test)
# ==========================================
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ==========================================
# 3. Train Logistic Regression Model
# ==========================================
# max_iter=3000 is used to give the solver enough time to find the best curve
log_reg = LogisticRegression(max_iter=3000) 
log_reg.fit(X_train, y_train)

# ==========================================
# 4. Make Predictions
# ==========================================
y_pred = log_reg.predict(X_test)

# ==========================================
# 5. Evaluate
# ==========================================
acc = accuracy_score(y_test, y_pred)
print(f"Accuracy Score: {acc:.4f}")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# ==========================================
# 6. Check Coefficients (a1, a2...) and Intercept (a0)
# ==========================================
print("\nIntercept (a0):", log_reg.intercept_[0])
print("First 5 Coefficients (a1, a2...):", log_reg.coef_[0][:5])
