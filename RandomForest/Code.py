import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns

# ==========================================
# 1. Load Dataset
# ==========================================
# The digits dataset contains 8x8 images of handwritten numbers (0-9)
digits = load_digits()

# Create a DataFrame just to see the data structure (optional)
df = pd.DataFrame(digits.data, columns=digits.feature_names)
df['target'] = digits.target

print("Data Shape:", df.shape) # (1797 rows, 64 columns + 1 target)
print(df.head())
print("-" * 30)

# ==========================================
# 2. Split Data
# ==========================================
X = digits.data
y = digits.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ==========================================
# 3. Train Random Forest Model
# ==========================================
# n_estimators=100: It will build 100 separate Decision Trees.
# The final answer will be the Majority Vote of these 100 trees.
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# ==========================================
# 4. Evaluate
# ==========================================
y_pred = rf.predict(X_test)
acc = accuracy_score(y_test, y_pred)

print(f"Accuracy Score: {acc:.4f}") # Usually very high (around 0.97+)

# ==========================================
# 5. Visualize Confusion Matrix
# ==========================================
# This shows us where the model got confused (e.g., confusing '3' with '8')
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(8,6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix for Random Forest')
plt.show()

# ==========================================
# 6. Check a Specific Prediction
# ==========================================
# Let's pick a random image from the test set
idx = 0
predicted_val = rf.predict([X_test[idx]])
actual_val = y_test[idx]

print(f"Check Index {idx}: Predicted {predicted_val[0]}, Actual {actual_val}")
