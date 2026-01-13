## 1. What is Feature Scaling?

### Definition
**Feature Scaling** is a data preprocessing technique used to standardize independent features into a fixed range. It is applied when features have very different magnitudes, units, or value ranges.

### Why do we need it?
Many Machine Learning algorithms (such as **K-Nearest Neighbors, Support Vector Machines, and Linear Regression**) calculate distances between data points.

If one feature has large values (e.g., `Salary = 100,000`) and another has small values (e.g., `Age = 25`), the algorithm may incorrectly treat the larger-valued feature as more important.

**Feature scaling solves this problem** by bringing all features onto the same scale, allowing the model to treat them equally.

### Real-World Example
Imagine you are comparing two people:

- **Person A:** Age = 30, Salary = 50,000  
- **Person B:** Age = 50, Salary = 55,000  

The difference in age is only **20**, but the difference in salary is **5,000**.  
Without scaling, the model focuses mainly on salary and ignores age.

Feature scaling converts both features into a small, comparable range (such as **0 to 1**), ensuring fair contribution from each feature.

---

## 2. Types of Feature Scaling

There are two commonly used feature scaling techniques:

- **Standardization**
- **Normalization**

---

### A. Standardization (Z-Score Scaling)

#### What it does
Standardization transforms data so that it is centered around **0**.

#### How it works
It measures how many **standard deviations** a value is away from the mean.

- Mean (μ) becomes **0**
- Standard Deviation (σ) becomes **1**

#### When to use
- Default choice for many ML algorithms
- Works well with **SVM, Neural Networks, Logistic Regression**
- Handles **outliers** better than normalization

---
<img width="3999" height="2908" alt="image" src="https://github.com/user-attachments/assets/f002ee5b-e421-4aae-b247-ee3f2534802a" />

---

### B. Normalization (Min-Max Scaling)

#### What it does
Normalization rescales data into a fixed range, usually **0 to 1**.

#### How it works
- Minimum value becomes **0**
- Maximum value becomes **1**
- Values are scaled based on the total range

#### When to use
- When feature distribution has a small standard deviation
- Commonly used in **Deep Learning**, especially **CNNs**, where pixel values must be between 0 and 1
