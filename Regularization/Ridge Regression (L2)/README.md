# Regularization: Ridge Regression (L2)

## 1. What is Regularization?

**Regularization** is a technique used to fix **Overfitting** in Machine Learning models.

**Concept:**  
It intentionally adds a **penalty (burden)** to the model during training.

**Why?**  
To stop the model from becoming too complex and memorizing noise instead of learning the true pattern.

---

## 2. The Problem: Overfitting in Linear Regression

### What is Overfitting?

Overfitting occurs when a model learns the **training data too well**.

**Result:**  
- Very high (sometimes 100%) accuracy on training data  
- Very poor performance on testing (unseen) data  

---

### How to Detect Overfitting in Linear Regression?

You can inspect the **weights (slopes / \(m\))**:

- **High Weights (very large \(m\))**  
  - Model is **Overfitting**  
  - Line becomes extremely steep or curvy to pass through every point  

- **Very Low Weights (near zero \(m\))**  
  - Model is **Underfitting**  
  - Model is too simple and fails to learn  

- **Moderate Weights**  
  - Model is a **Good Fit**  

---

## 3. The Solution: Ridge Regression (L2)

**Ridge Regression** is a modified version of Linear Regression that **forces the weights to remain small**.

### Why is it called **L2**?

- The penalty uses the **square of the weights** (\(m^2\))
- Squaring corresponds to the **L2 norm**

> **Note:**  
> - **L1 Regularization** uses \(|m|\) → Lasso Regression  
> - **L2 Regularization** uses \(m^2\) → Ridge Regression  

---

## 4. The Ridge Regression Formula

### Normal Linear Regression Objective

We minimize only the **error (loss)**:

$$
\sum (y - \hat{y})^2
$$

---

### Ridge Regression Objective

We minimize **Error + Penalty**:

$$
\text{New Loss} = \sum (y - \hat{y})^2 + \lambda m^2
$$

- **First Term:** Keeps predictions accurate  
- **Second Term:** Penalizes large weights  

---

### For Multiple Features

If the model has multiple weights \(m_1, m_2, m_3, \dots\), the penalty becomes:

$$
\text{Penalty} = \lambda (m_1^2 + m_2^2 + m_3^2 + \dots)
$$

---

## 5. How the Penalty Works (Intuition)

Imagine the model tries to use a huge weight:

- \(m = 1000\)

### Normal Linear Regression
> "Great! Training error is zero."

### Ridge Regression
> "Not so fast!"

The penalty becomes:

$$
\lambda \times 1000^2 = 1{,}000{,}000 \times \lambda
$$

This massively increases the loss.

---

### Result

- The model is **forced to choose smaller weights** (e.g., \(m = 3\))
- It sacrifices a little training accuracy
- But gains much better **generalization**

---

## 6. Role of Lambda (\(\lambda\))

\(\lambda\) is a **hyperparameter** you choose.

- **\(\lambda = 0\)**  
  - No penalty  
  - Same as normal Linear Regression  

- **Small \(\lambda\)**  
  - Light penalty  
  - Slight regularization  

- **Large \(\lambda\)**  
  - Strong penalty  
  - Weights shrink close to zero  
  - Can cause **underfitting**

---

**Summary:**  
Ridge Regression controls overfitting by **shrinking weights**, keeping the model simple, stable, and better at handling unseen data.
