import numpy as np
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# ==========================================
# 1. Generate Data
# ==========================================
# make_regression creates a random dataset for regression problems
X, y = make_regression(n_samples=100, n_features=1, n_informative=1, n_targets=1, noise=20, random_state=13)

# Split into Train and Test (Optional, but good practice)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

# ==========================================
# 2. Define Custom Gradient Descent Class
# ==========================================
class GDRegressor:

    def __init__(self, learning_rate, epochs):
        self.m = 100   # Random starting Slope (Weight)
        self.b = -120  # Random starting Intercept (Bias)
        self.lr = learning_rate
        self.epochs = epochs

    def fit(self, X, y):
        # The Loop (Training Process)
        for i in range(self.epochs):
            
            # Calculate Slope of Loss with respect to b (Intercept)
            # Formula: -2 * sum(y_true - y_pred)
            loss_slope_b = -2 * np.sum(y - self.m * X.ravel() - self.b)
            
            # Calculate Slope of Loss with respect to m (Coefficient)
            # Formula: -2 * sum((y_true - y_pred) * x)
            loss_slope_m = -2 * np.sum((y - self.m * X.ravel() - self.b) * X.ravel())

            # Update Parameters (Gradient Descent Step)
            # b_new = b_old - (learning_rate * slope)
            self.b = self.b - (self.lr * loss_slope_b)
            self.m = self.m - (self.lr * loss_slope_m)
            
        print(f"Training Complete! Final m: {self.m:.2f}, Final b: {self.b:.2f}")

    def predict(self, X):
        # y = mx + b
        return self.m * X + self.b

# ==========================================
# 3. Run the Code
# ==========================================

# Create the object (Learning Rate=0.001, Iterations=50)
gd = GDRegressor(learning_rate=0.001, epochs=50)

# Train the model
gd.fit(X_train, y_train)

# Make a prediction
y_pred = gd.predict(X_test)

# ==========================================
# 4. Check Results (Optional Visualization)
# ==========================================
# Just to show you it actually learned the line
print("Prediction for first test value:", y_pred[0])
print("Actual value:", y_test[0])

# Plotting
plt.scatter(X, y, color='blue', label='Data')
plt.plot(X_train, gd.predict(X_train), color='red', label='GD Line')
plt.legend()
plt.title('Custom Gradient Descent')
plt.show()
