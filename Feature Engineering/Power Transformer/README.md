## Power Transformer

### 1. What is Power Transformer?

Similar to the **Function Transformer**, a **Power Transformer** is used to change the shape of data so that it becomes closer to a **Normal Distribution (Bell Curve)**.

#### Difference from Function Transformer

- **Function Transformer:**  
  You manually choose the mathematical function (such as Log, Square, or Square Root).

- **Power Transformer:**  
  It is more **intelligent and automated**.  
  It automatically finds the best mathematical **power value (λ)** that makes the data as normally distributed as possible.  
  The transformer tests multiple values and selects the most suitable one.

---

### 2. Types of Power Transformations

Power Transformer provides two main transformation methods:

---

#### A. Box-Cox Transformation

**Requirement:**  
- Works **only with positive values** (`> 0`)

**Limitation:**  
- If the dataset contains **zero or negative values** (e.g., `0`, `-5`, `-10`), Box-Cox will throw an error.

**Formula:**  
Uses a power parameter **λ (lambda)** to transform the data:

\[
(x^\lambda - 1) / \lambda
\]

---

#### B. Yeo-Johnson Transformation

**Requirement:**  
- Works with **positive, negative, and zero values**

**Advantage:**  
- An enhanced and more flexible version of Box-Cox  
- Safest default choice when the data distribution is unknown  
- Does not fail on zero or negative values

---

