## Gradient Descent

### 1. What is Gradient Descent?

**Gradient Descent** is an **Optimization Algorithm**.

**Goal:**  
To find the **minimum value (minima)** of any differentiable function.

#### Simple Analogy  
Imagine you are standing on top of a mountain (**high error / loss**) while blindfolded, and you want to reach the bottom of the valley (**minimum error**).

- You feel the ground with your feet  
- Find the **steepest downward slope**  
- Take small steps in that direction  
- Stop when the ground becomes flat  

This is exactly how Gradient Descent works.

---

### 2. Types of Gradient Descent

There are three main variants based on how much data is used in each update:

- **Batch Gradient Descent**  
  - Uses the **entire dataset** to calculate the gradient  
  - Updates the model once per epoch  
  - Accurate  
  - Slow for large datasets  

- **Stochastic Gradient Descent (SGD)**  
  - Uses **only one random data point** per update  
  - Updates very frequently  
  - Very fast  
  - Noisy, zig-zag path  

- **Mini-Batch Gradient Descent**  
  - Uses a **small batch** (e.g., 32 or 64 samples)  
  - Combines speed and stability  
  - Most commonly used in practice  

---

### 3. How Gradient Descent Works (Step-by-Step)

#### Step 1: Initialization  
Start with random values for the parameters (e.g., \(m\) and \(b\)).  
Example:  
\[
b = 0
\]

---

#### Step 2: Calculate the Slope (Gradient)

- Find the slope of the **Loss Function** at the current point  
- If slope is **positive (+)** → subtract to go down  
- If slope is **negative (-)** → subtract to go down  

To handle both cases mathematically, we **always subtract the gradient**:

\[
b_{\text{new}} = b_{\text{old}} - \text{Slope}
\]

---

#### Step 3: Learning Rate (Step Size)

Directly subtracting the slope may cause **overshooting** (jumping across the valley).

To control this, we multiply the slope by a small number called the  
**Learning Rate (\(\eta\) or \(\alpha\))**.

\[
b_{\text{new}} = b_{\text{old}} - (\text{Learning Rate} \times \text{Slope})
\]

**Common learning rate values:**  
- \(0.01\)  
- \(0.001\)

---

#### Step 4: Convergence (When to Stop?)

Since Gradient Descent is **iterative**, we stop when:

- **Max iterations reached**  
  - Example: 1000 epochs  
- **Change becomes very small**  
  - \(|b_{\text{new}} - b_{\text{old}}| < 0.0001\)

This means the algorithm has reached the minimum.

---

### 4. Mathematical Formulation

#### A. Updating One Variable (\(b\))

\[
b_{\text{new}} = b_{\text{old}} - \eta \cdot \frac{\partial L}{\partial b}
\]

Where:
- \(\eta\) = Learning Rate  
- \(\frac{\partial L}{\partial b}\) = Gradient of the loss w.r.t \(b\)

---

#### B. Updating Both \(m\) and \(b\) (Linear Regression)

For the model:

\[
y = mx + b
\]

Steps:
- Initialize random \(m\) and \(b\)  
- Set epochs = 100, learning rate = 0.01  
- Update both parameters simultaneously  

\[
b_{\text{new}} = b_{\text{old}} - (\text{Learning Rate} \times \text{Slope}_b)
\]

\[
m_{\text{new}} = m_{\text{old}} - (\text{Learning Rate} \times \text{Slope}_m)
\]

---

### 5. Important Concepts & Problems

#### A. Effect of Loss Function Shape

**Convex Loss Function (Bowl-shaped)**  
- Only **one minimum** (Global Minimum)  
- Gradient Descent **always finds it**

**Non-Convex Loss Function (Wavy-shaped)**  
- Multiple valleys  
- **Local Minima**: Small valley, not the best solution  
- **Global Minima**: Deepest valley (best solution)

**Problem:**  
Gradient Descent may get **stuck in a Local Minimum** and miss the Global Minimum.
<img width="3999" height="3999" alt="image" src="https://github.com/user-attachments/assets/387832ef-6a64-4547-805a-96086a099654" />

---
### B. Effect of Learning Rate (\(\eta\))

The **Learning Rate** controls **how big a step** Gradient Descent takes while moving toward the minimum.

- **Too Low (e.g., 0.00001)**  
  - The model takes **very tiny steps**  
  - Convergence is extremely slow  
  - Computationally expensive  
  - Takes a long time to reach the minimum  

- **Too High (e.g., 1.0)**  
  - The model takes **giant steps**  
  - Overshoots the minimum  
  - Causes zig-zag movement  
  - May diverge and never converge  

- **Just Right**  
  - Steps are **small enough to be stable**  
  - Steps are **large enough to be fast**  
  - Smooth and efficient convergence  

**Key Idea:**  
Choosing the correct learning rate is critical. A bad value can completely break Gradient Descent, while a good value helps it converge quickly and smoothly.
