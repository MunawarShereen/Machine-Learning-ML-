import numpy as np
from sklearn.datasets import load_iris, load_digits
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import Binarizer

# ==========================================
# 1. Gaussian Naive Bayes (Continuous Data)
# ==========================================
print("--- 1. Gaussian Naive Bayes (Iris Dataset) ---")
# Iris data has continuous features like 5.1, 3.5, 1.4, 0.2
data_iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(data_iris.data, data_iris.target, test_size=0.2, random_state=42)

gnb = GaussianNB()
gnb.fit(X_train, y_train)
y_pred_gnb = gnb.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, y_pred_gnb):.4f}")
print("Example Data (Continuous):", X_test[0])


# ==========================================
# 2. Multinomial Naive Bayes (Count/Frequency Data)
# ==========================================
print("\n--- 2. Multinomial Naive Bayes (Digits Dataset) ---")
# Digits data has integer values (0 to 16) representing pixel intensity (counts)
data_digits = load_digits()
X_train, X_test, y_train, y_test = train_test_split(data_digits.data, data_digits.target, test_size=0.2, random_state=42)

mnb = MultinomialNB()
mnb.fit(X_train, y_train)
y_pred_mnb = mnb.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, y_pred_mnb):.4f}")
print("Example Data (Discrete Counts):", X_test[0][:10]) # First 10 pixels


# ==========================================
# 3. Bernoulli Naive Bayes (Binary Data)
# ==========================================
print("\n--- 3. Bernoulli Naive Bayes (Binarized Digits) ---")
# We take the same Digits data but convert it to strictly 0 or 1
# If pixel value > 0 -> 1 (Ink present)
# If pixel value = 0 -> 0 (No Ink)
binarizer = Binarizer(threshold=0.0) # Threshold 0.0 means anything > 0 becomes 1
X_binary = binarizer.fit_transform(data_digits.data)

X_train, X_test, y_train, y_test = train_test_split(X_binary, data_digits.target, test_size=0.2, random_state=42)

bnb = BernoulliNB()
bnb.fit(X_train, y_train)
y_pred_bnb = bnb.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, y_pred_bnb):.4f}")
print("Example Data (Binary):", X_test[0][:10]) # First 10 pixels are now 0 or 1
