import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score

# ==========================================
# 1. Load Data
# ==========================================
# Using the classic Iris dataset (Flower classification)
data = load_iris()
X = data.data
y = data.target

# ==========================================
# 2. Split Data
# ==========================================
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ==========================================
# 3. Train Decision Tree Model
# ==========================================
# criterion='entropy': This tells the model to use Information Gain (ID3 style)
# max_depth=3: We limit the tree depth to 3 to keep it simple and readable
clf = DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=42)
clf.fit(X_train, y_train)

# ==========================================
# 4. Make Predictions & Evaluate
# ==========================================
y_pred = clf.predict(X_test)

print(f"Accuracy Score: {accuracy_score(y_test, y_pred):.4f}")
print("-" * 30)

# ==========================================
# 5. Visualize the Tree
# ==========================================
plt.figure(figsize=(12, 8))
plot_tree(clf, 
          filled=True, 
          feature_names=data.feature_names, 
          class_names=data.target_names,
          rounded=True)

plt.title("Decision Tree Visualization (Using Entropy)")
plt.show()
