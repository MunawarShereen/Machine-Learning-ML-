## Linear Regression

### 1. What is Linear Regression?

**Linear Regression** is the *“Hello World”* of Machine Learning.  
It is a **Supervised Learning** algorithm used for **Regression tasks**, where the goal is to predict **numerical values** such as:

- Salary  
- House Price  
- Temperature  

**Goal:**  
To find the **Best Fit Line** that passes through the data points with **minimum error**.

<img width="3000" height="2000" alt="image" src="https://github.com/user-attachments/assets/28474827-a8db-4c61-8c72-5e1e8eece656" />

---

### 2. Why Study It First?

There is a reason why almost every Machine Learning course starts with Linear Regression:

- **Easy to Understand:**  
  Based on simple high-school mathematics:  
  \[
  y = mx + c
  \]

- **Strong Foundation:**  
  Many advanced algorithms (Logistic Regression, Neural Networks) are built on top of Linear Regression.

- **Highly Interpretable:**  
  You can clearly explain model decisions, e.g.,  
  *“Salary increased because Experience increased.”*

---

### 3. Types of Linear Regression

There are **four main variations**, depending on data complexity.

---

#### 1. Simple Linear Regression

**Definition:**  
Used when there is **one input feature** and **one output target**.

**Equation:**
\[
y = mx + b
\]

Where:
- \(y\) → Output (Target)
- \(x\) → Input (Feature)
- \(m\) → Slope (Weight / Importance)
- \(b\) → Intercept (Bias)

**Example:**  
Predicting **Weight** based only on **Height**.

---

#### 2. Multiple Linear Regression

**Definition:**  
Used when there are **multiple input features** and **one output**.

**Equation:**
\[
y = b_0 + b_1x_1 + b_2x_2 + \dots + b_nx_n
\]

This forms a **Plane** or **Hyperplane** in higher dimensions.

**Example:**  
Predicting **House Price** using:
- Size  
- Location  
- Number of Rooms  
- Age of the House  

---

#### 3. Polynomial Linear Regression

**Why do we need it?**  
Simple and Multiple Linear Regression assume a **straight-line (linear)** relationship.  
But real-world data is often **curved**.

**Definition:**  
We transform features into higher powers to capture non-linear patterns.

**Equation:**
\[
y = b_0 + b_1x + b_2x^2 + \dots
\]

**Example:**  
Predicting **Virus Growth**, which starts slowly and then increases rapidly.

---

#### 4. Regularization (Ridge & Lasso)

**Problem:**  
Linear Regression can **overfit** the training data by learning noise.

**Solution:**  
**Regularization** adds a **penalty term** to control model complexity.

**Types of Regularization:**

- **Lasso (L1 Regularization):**  
  - Can shrink some feature weights to **zero**  
  - Helps in **Feature Selection**

- **Ridge (L2 Regularization):**  
  - Shrinks weights close to zero  
  - Keeps all features but reduces their influence

---
