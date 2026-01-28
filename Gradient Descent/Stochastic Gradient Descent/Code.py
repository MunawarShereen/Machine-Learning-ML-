import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import r2_score

# 1. Load Data
X, y = load_diabetes(return_X_y=True)

# 2. Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

# 3. Initialize SGD Regressor
# max_iter: Number of epochs
# learning_rate='constant': Keeps the speed same throughout (no schedule)
# eta0: The learning rate value (0.01)
reg = SGDRegressor(max_iter=100, learning_rate='constant', eta0=0.01)

# 4. Train
reg.fit(X_train, y_train)

# 5. Predict
y_pred = reg.predict(X_test)

# 6. Check Score
print("R2 Score:", r2_score(y_test, y_pred))
