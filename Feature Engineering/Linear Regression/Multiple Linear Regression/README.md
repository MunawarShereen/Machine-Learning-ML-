## Multiple Linear Regression (MLR)

### 1. What is Multiple Linear Regression?

In **Simple Linear Regression**, we use only **one input feature** to predict the output  
(e.g., *Study Hours → Marks*).

However, real-world problems are rarely that simple.  
Most outcomes depend on **multiple factors**.

**Multiple Linear Regression (MLR)** is a technique where we use **multiple input columns** to predict **one output column**.

#### Example: Predicting House Price

- **Input 1 (\(x_1\))**: Size of the house  
- **Input 2 (\(x_2\))**: Number of rooms  
- **Input 3 (\(x_3\))**: Location score  
- **Output (\(y\))**: House price  

---

### 2. Visualizing the Geometry (Shapes)

As we increase the number of input features, the shape of the model changes:

- **2D (1 Input):** A **Line**
- **3D (2 Inputs):** A **Plane** (like a flat sheet floating in space)
- **4D or Higher (n Inputs):** A **Hyperplane**

> **Note:** Humans cannot visualize 4D or higher dimensions, but the mathematics works exactly the same way.

---

### 3. The Mathematical Formula

Because we have multiple inputs, the equation \(y = mx + b\) expands.

#### Specific Formula (2 Inputs)

\[
y = m_1x_1 + m_2x_2 + b
\]

---

#### General Formula (Standard Notation)

\[
y = \beta_0 + \beta_1x_1 + \beta_2x_2 + \dots + \beta_nx_n
\]

---

#### Summation Form

\[
y = \beta_0 + \sum_{i=1}^{n} \beta_i x_i
\]

---

### 4. Explanation of Terms

- **\(y\)**: The value we want to predict (target)
- **\(\beta_0\)**: Intercept (Bias)  
  - Value of \(y\) when all inputs are 0
- **\(\beta_1, \beta_2, \dots\)**: Coefficients (Weights)  
  - Represent the importance of each input feature

**Example:**  
If **\(\beta_1\)** is large, it means **\(x_1\)** has a strong influence on the output.

---
