from sklearn.datasets import load_diabetes
import numpy as np
from sklearn.linear_model import LinearRegression, SGDRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import random

# ==========================================
# 1. Load and Prepare Data
# ==========================================
X, y = load_diabetes(return_X_y=True)

# Split into Train and Test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

# ==========================================
# 2. Mini-Batch Gradient Descent Logic
# ==========================================

# We use SGDRegressor because it allows 'partial_fit' (updating model one piece at a time)
sgd = SGDRegressor(learning_rate='constant', eta0=0.01)

batch_size = 35
epochs = 100

for i in range(epochs):
    
    # Randomly select 'batch_size' number of rows (indices) from the training data
    idx = random.sample(range(X_train.shape[0]), batch_size)
    
    # Update the model using ONLY that batch
    # partial_fit updates weights without forgetting what it learned before
    sgd.partial_fit(X_train[idx], y_train[idx])

# ==========================================
# 3. Check Accuracy
# ==========================================
y_pred = sgd.predict(X_test)

score = r2_score(y_test, y_pred)
print(f"R2 Score (Accuracy): {score:.4f}")
