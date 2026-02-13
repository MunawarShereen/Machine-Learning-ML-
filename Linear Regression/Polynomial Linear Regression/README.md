# Polynomial Linear Regression

## 1. Why Do We Need It? (The Problem)

Simple Linear Regression works well when the relationship between variables is a **straight line**.

But in real life, data is often **non-linear (curved)**.

If you try to fit a straight line:

$$
y = mx + b
$$

to curved data (like a parabola), the model will perform poorly.  
It will be **too rigid** to capture the true pattern.

### Solution
Use **Polynomial Regression** to fit a **curve** instead of a straight line.

---

## 2. What is Polynomial Regression?

Polynomial Regression is a special case of **Linear Regression** where the relationship between:

- Independent variable x
- Dependent variable y

is modeled as an **n-th degree polynomial**.

### Key Concept

We "trick" the Linear Regression model.

- The model itself is still **linear**
- But we **transform the input features** (e.g., square or cube them)

---

## 3. The Formula

### Simple Linear Regression (Degree 1)

$$
y = \beta_0 + \beta_1 x
$$

**Result:** Straight line

---

### Polynomial Regression (Degree 2 — Quadratic)

$$
y = \beta_0 + \beta_1 x + \beta_2 x^2
$$

**Result:** Parabola / Curve

---

### Polynomial Regression (Degree n)

$$
y = \beta_0 + \beta_1 x + \beta_2 x^2 + \beta_3 x^3 + \dots + \beta_n x^n
$$

Where:

- $\( \beta_0 \)$: Intercept (Bias)
- $\( \beta_1, \beta_2, \dots, \beta_n \)$: Coefficients (Weights)
- $\( x^2, x^3, \dots \)$: Polynomial features

---

## 4. How It Works: Feature Transformation

Linear Regression only knows how to draw **straight lines**.

So how do we get a curve?

We use **Polynomial Feature Transformation**.

---

### Step 1: Input Data

Suppose we have one feature:

- Size x 

---

### Step 2: Transformation (Preprocessing)

We create new features:

- Column 1 → $\ x $
- Column 2 → $\ x^2 $
- Column 3 → $\ x^3 $

These are called **polynomial features**.

---

### Step 3: Training

We feed these transformed columns into a **Multiple Linear Regression** model.

The model now thinks it has multiple independent features:

- $\ x $
- $\ x^2 $
- $\ x^3 $

It calculates optimal weights for each.

When plotted, the final prediction looks like a **smooth curve**.

---

## 5. The Degree (Hyperparameter)

The most important setting in Polynomial Regression is the **Degree**.

### Low Degree (e.g., 1)

- Creates a straight line
- Problem: **Underfitting**
- Too simple to capture complex patterns

---

### Optimal Degree (e.g., 2 or 3)

- Creates a smooth curve
- Good balance
- Captures the trend properly

---

### High Degree (e.g., 20)

- Creates a very wiggly curve
- Problem: **Overfitting**
- Memorizes noise instead of learning the true pattern

---

## Final Takeaway

Polynomial Regression allows Linear Regression to model **non-linear relationships** by transforming input features into polynomial terms.
