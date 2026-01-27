## Batch Gradient Descent (For Multiple Dimensions)

### 1. Introduction: From Simple to Multiple

In the simple case of Linear Regression:

\[
y = mx + b
\]

we had:
- **One input feature** (\(x\))
- **Two parameters to learn** (\(m\) and \(b\))

But in real-world problems, outputs depend on **multiple inputs**.

**Example:**  
House Price depends on **Size, Rooms, Location, Age**, etc.

So the equation becomes:

$$
y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_3 x_3 + \dots + \beta_n x_n
$$

Now, instead of updating just \(m\) and \(b\), we must update **all parameters**:

\[
\beta_0, \beta_1, \beta_2, \dots, \beta_n
\]

**All of them are updated simultaneously.**

---

### 2. What is *Batch* Gradient Descent?

The word **Batch** means **“the entire dataset”**.

In **Batch Gradient Descent**, the model:
- Looks at **all rows**
- Calculates the **total error**
- Then takes **one single step** to update the weights

One update = one full pass over the dataset.

---

### 3. How Batch Gradient Descent Works

#### Step 1: Initialization (Starting Point)

Before learning begins:
- The algorithm checks how many input features you have.
- For **\(n\)** features, it creates:
  - **\(n\) weights**: \(\beta_1, \beta_2, \dots, \beta_n\)
  - **1 intercept**: \(\beta_0\)

All parameters are initialized to a default value (usually **0 or 1**).

This is just a **rough guess**.

---

#### Step 2: Batch Prediction (Vectorization)

Instead of predicting row-by-row, the model uses **matrix multiplication**.

- **Input Matrix**: \(X\) (all rows × all features)
- **Weight Vector**: \(\beta\)

Prediction for all rows at once:

\[
\hat{y} = X \cdot \beta
\]

This generates predictions for **every row simultaneously**  
Much faster than loops  
Used in real ML systems

---

#### Step 3: Calculating the Gradient (Slope)

Now the model measures **how wrong** the predictions are.

**Error vector:**

\[
\text{Error} = \hat{y} - y
\]

---

##### A. Gradient for the Intercept (\(\beta_0\))

Since \(\beta_0\) affects **every row equally**, its gradient is the **mean error**:

\[
\frac{\partial L}{\partial \beta_0}
= \frac{1}{m} \sum_{i=1}^{m} (\hat{y}_i - y_i)
\]

---

##### B. Gradient for the Weights (\(\beta_1, \beta_2, \dots\))

Each feature contributes differently to the error.

The gradient for all weights together is:

\[
\nabla_{\beta}
= \frac{1}{m} X^T (\hat{y} - y)
\]

This uses a **dot product** to calculate how responsible each feature is for the total error.

---

#### Step 4: Updating the Weights (Learning Step)

Once gradients are computed, parameters are updated using the **Learning Rate (\(\eta\))**.

**Update Rule:**

\[
\beta_{\text{new}} = \beta_{\text{old}} - \eta \cdot \nabla_{\beta}
\]

This moves the weights **closer to the minimum loss**.

---

#### Step 5: Iteration (Training Loop)

Steps **2 → 3 → 4** are repeated multiple times.

- Each repetition is called an **Epoch**
- With every epoch:
  - Error decreases
  - Weights improve
- Training stops when:
  - Max epochs are reached, or
  - Loss converges

Final goal: **Global Minimum (best possible solution)**

---

### 4. Pros and Cons

| Advantages | Disadvantages |
|---------|--------------|
| Stable: Smooth convergence (no zig-zag) | Slow: Uses entire dataset for one update |
| Vectorized: Efficient with matrix math | Memory Heavy: Needs full dataset in RAM |
| Guaranteed convergence for convex loss | Not suitable for Big Data / streaming data |

---

**Summary:**  
Batch Gradient Descent is **mathematically clean, stable, and reliable**, but becomes **slow and memory-intensive** as data size grows.
