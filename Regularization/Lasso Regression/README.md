# Lasso Regression (L1 Regularization)

## 1. What is Lasso Regression?

**Lasso** stands for **Least Absolute Shrinkage and Selection Operator**.

Just like **Ridge Regression**, it is a regularization technique used to reduce **overfitting**.

However, Lasso has a **special superpower** that Ridge does not have:

**It can completely remove useless features.**

---

## 2. The Formula (L1 Penalty)

In **Ridge Regression (L2)**, we penalize the **square of the weights** $\w^2$.

In **Lasso Regression (L1)**, we penalize the **absolute value of the weights** $\|w|$.

$$
\text{New Loss} = \sum (y - \hat{y})^2 + \lambda |w|
$$

- **First Part:** Minimize prediction error  
- **Second Part:** Minimize the size of weights (keep the model simple)  

$\lambda$ (**Lambda**) controls the **strength of the penalty**.

---

## 3. Lasso vs. Ridge (Key Differences)

| Feature | Ridge Regression (L2) | Lasso Regression (L1) |
|------|----------------------|----------------------|
| Penalty | Adds $\w^2$ (square) | Adds $\|w|$ (absolute value) |
| Effect on Weights | Shrinks weights close to zero (e.g., 0.0001) | Shrinks weights to **exactly zero** |
| Feature Selection | No (keeps all features) | Yes (removes useless features) |
| Best Used For | When all features matter | When many features are useless |

---

## 4. Why Does Lasso Perform Feature Selection?

As **$\lambda$** increases in Lasso:

- The penalty becomes stronger  
- The model reduces unnecessary weights to **zero**  
- Features with zero weight are **removed from the equation**

### Example:

$$
y = 3(\text{Size}) + 0(\text{Color}) + 5(\text{Rooms})
$$

Here, the **Color** feature is completely removed.

---

## 5. Lasso Sparsity

**Sparsity** means a model where **most values are zero**.

- Increasing $\lambda$ in Lasso causes more coefficients to become zero  
- This results in a **Sparse Model**  
- Sparse models are simpler and easier to interpret  

 **Warning:**  
If $\lambda$ is too large, **all coefficients become zero**, leading to **underfitting** (the model learns nothing).

---

## 6. When Should You Use Lasso?

Use **Lasso Regression** when:

- **High-Dimensional Data:**  
  You have many features (e.g., 1000 columns) but only a few are useful  

- **Automatic Feature Selection:**  
  You want the model to tell you which features are important and which are trash  

---

**Summary:**  
Lasso Regression not only reduces overfitting but also **automatically selects features**, making it extremely powerful for high-dimensional datasets.
