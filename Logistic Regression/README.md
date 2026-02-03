# Logistic Regression

## 1. What is Logistic Regression?

Logistic Regression is a **Supervised Classification Model**.

Unlike **Linear Regression**, which predicts a continuous number, **Logistic Regression predicts a Category (Probability)**.

- **Dependent Variable (y):** Must be **Categorical**, usually **Binary (0 or 1)**
- **Examples:** Yes / No, Spam / Not Spam, Pass / Fail
- **Goal:** Classify data into classes based on input features

---

## 2. The Core: Sigmoid Function

In Linear Regression, predictions can range from **−∞ to +∞**, which is meaningless for probabilities.

Probabilities must always lie between **0 and 1**.

To solve this, Logistic Regression uses the **Sigmoid Function**.

### Role of Sigmoid
- Converts any real value into a number between **0 and 1**
- Makes probability interpretation possible

### Shape
- Produces an **S-shaped curve** (Sigmoid Curve)
- Unlike Linear Regression’s straight line

### Formula

$$
y = \frac{1}{1 + e^{-z}}
$$

Where:
- \( y \): Predicted probability (0 to 1)
- \( e \): Euler’s number (≈ 2.718)
- \( z \): Linear equation output

---

## 3. Understanding the Equation

The value \( z \) comes from a **linear equation**, similar to Linear Regression:

$$
z = a_0 + a_1 x
$$

- **\( a_0 \) (Intercept):**  
  Baseline value (bias) — shifts the curve left or right

- **\( a_1 \) (Coefficient):**  
  Weight of the feature  
  Indicates how much the **log-odds** of \( y \) change when \( x \) increases by 1 unit

**Interpretation:**
- If \( a_1 > 0 \): Increasing \( x \) increases the probability of class 1
- If \( a_1 < 0 \): Increasing \( x \) decreases the probability of class 1

---

## 4. Linear vs. Logistic Regression (Comparison)

| Feature | Linear Regression | Logistic Regression |
|------|-----------------|-------------------|
| Type | Supervised Regression | Supervised Classification |
| Output (y) | Continuous (Price, Temperature) | Categorical / Binary (0 or 1) |
| Range | −∞ to +∞ | 0 to 1 (Probability) |
| Best Fit Shape | Straight Line | S-Shaped Curve (Sigmoid) |
| Used For | Predicting **How much?** | Predicting **Which one?** |
