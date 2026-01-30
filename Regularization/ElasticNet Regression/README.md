# ElasticNet Regression

## 1. What is ElasticNet?

**ElasticNet Regression** is the **hybrid child** of **Ridge** and **Lasso** Regression.  
It combines the strengths of both techniques.

- **Ridge (L2):**  
  Used when all features are important. It shrinks weights but keeps all features.

- **Lasso (L1):**  
  Used when some features are useless. It can delete features by setting weights to zero.

- **ElasticNet:**  
  Used when you are unsure. You have many columns and don’t know which features matter.

---

## 2. Why Do We Need ElasticNet?

### The “Unknown” Scenario

If you have **100 features** and you don’t know:
- whether to delete some (Lasso), or
- keep all of them (Ridge),

 **ElasticNet automatically finds a balance.**

---

### Multicollinearity (Very Important)

When features are **highly correlated**  
(e.g., *Weight in kg* and *Weight in lbs*):

- **Lasso:** Randomly keeps one feature and deletes the other (risky)
- **Ridge:** Keeps both features
- **ElasticNet:** Treats them as a group  
  → Either keeps both or drops both

This makes ElasticNet **safer and more stable**.

---

## 3. The Formula (Loss Function)

ElasticNet adds **both penalties** to the loss function.

$$
\text{Loss} = \sum (y - \hat{y})^2 + a|w|^2 + b|w|
$$

- **First Part:** Mean Squared Error (MSE)
- **Second Part $\(a|w|^2\)$:** Ridge penalty (L2)
- **Third Part $\(b|w|\)$:** Lasso penalty (L1)

---

## 4. Hyperparameters $\lambda$ and Ratio)

Instead of directly setting $\a$ and $\b$, we control two simpler parameters.

### A. Lambda $\lambda$ / Alpha

Represents the **total penalty strength**:

$$
\lambda = a + b
$$

- Larger $\lambda$ → stronger regularization
- Smaller $\lambda$ → weaker regularization

---

### B. L1 Ratio

Tells us how much **Lasso** is mixed into ElasticNet.

- `l1_ratio = 1` → Pure Lasso
- `l1_ratio = 0` → Pure Ridge
- `l1_ratio = 0.5` → 50% Lasso + 50% Ridge (default)

---
$$
l1ratio = \frac{a}{a + b}
$$


---

## 5. Summary Table

| Feature | Ridge (L2) | Lasso (L1) | ElasticNet |
|------|-----------|-----------|-----------|
| Penalty | Square $\(w^2)$ | Absolute w | Both L1 + L2 |
| Feature Selection | No | Yes | Partial |
| Best Used When | All features are useful | Many features are useless | Uncertain / High Multicollinearity |

---

**Summary:**  
ElasticNet is the **most flexible regularization method**, combining the stability of Ridge with the feature selection power of Lasso.
