import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import KNNImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# ==========================================
# 1. Make Your Own Data
# ==========================================
# Creating a dictionary with data simulating Titanic (Age, Fare, Family, Survived)
data = {
    'Age': [22, 38, 26, 35, 35, np.nan, 54, 2, 27, 14] * 10,  # Repeating to make 100 rows
    'Fare': [7.25, 71.28, 7.92, 53.1, 8.05, 8.45, 51.86, 21.07, 11.13, 30.07] * 10,
    'Family': [1, 1, 0, 1, 0, 0, 0, 4, 2, 1] * 10,
    'Survived': [0, 1, 1, 1, 0, 0, 0, 0, 1, 1] * 10
}

df = pd.DataFrame(data)

# Let's add more missing values randomly to make it realistic
np.random.seed(42) # For reproducibility
mask = np.random.choice([True, False], size=df.shape[0], p=[0.2, 0.8]) # 20% chance of True
df.loc[mask, 'Age'] = np.nan # Set 20% of Age to NaN

print("Original Data (First 5 Rows):")
print(df.head())
print("Missing Values in Age:", df['Age'].isnull().sum())
print("-" * 30)

# ==========================================
# 2. Split Data
# ==========================================
X = df.drop(columns=['Survived'])
y = df['Survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ==========================================
# 3. Apply KNN Imputer
# ==========================================
# It will look at 'Fare' and 'Family' to guess the missing 'Age'
knn = KNNImputer(n_neighbors=3, weights='distance')

# Fit and Transform on Training Data
X_train_trf = knn.fit_transform(X_train)

# Transform Test Data (using logic from Train)
X_test_trf = knn.transform(X_test)

# ==========================================
# 4. Train Model & Check Accuracy
# ==========================================
lr = LogisticRegression()
lr.fit(X_train_trf, y_train)

y_pred = lr.predict(X_test_trf)
print("Accuracy Score:", accuracy_score(y_test, y_pred))

# Optional: See what the filled values look like
X_train_filled = pd.DataFrame(X_train_trf, columns=X_train.columns)
print("\nData After Imputation (First 5 Rows):")
print(X_train_filled.head())
