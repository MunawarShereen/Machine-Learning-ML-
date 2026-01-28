# Mini-Batch Gradient Descent

## 1. What is Mini-Batch Gradient Descent?

Mini-Batch Gradient Descent is the **“sweet spot”** or middle ground between **Batch Gradient Descent** and **Stochastic Gradient Descent (SGD)**.

Instead of:
- using **all data** at once (Batch GD), or  
- using **only one row** at a time (Stochastic GD),

Mini-Batch GD uses a **small group of rows (a batch)** to update the weights.

### Analogy

- **Batch Gradient Descent**  
  A student studies the *entire textbook* before taking a mock test.  
  *(Very accurate but very slow)*

- **Stochastic Gradient Descent**  
  A student reads *one page* and immediately takes a test.  
  *(Very fast but chaotic)*

- **Mini-Batch Gradient Descent**  
  A student studies *one chapter (a small batch)* and then takes a test.  
  *(Balanced and practical approach)*

---

## 2. The Relationship (Batch Size)

The behavior of Mini-Batch Gradient Descent depends completely on the **Batch Size**.

- If **Batch Size = $N$ (total number of rows)**  
  → It becomes **Batch Gradient Descent**

- If **Batch Size = 1**  
  → It becomes **Stochastic Gradient Descent (SGD)**

- If **Batch Size is between $1$ and $N$**  
  → It is **Mini-Batch Gradient Descent**

### Common Batch Sizes
- 32  
- 64  
- 128  
- 256  

> Powers of 2 are preferred because they are more efficient for computer memory (RAM/GPU).

---

## 3. How it Works (The Process)

### Step 1: Shuffle  
Randomly shuffle the dataset.  
This is **very important** to remove bias.

### Step 2: Split  
Divide the dataset into small batches.

**Example:**  
If you have 1000 rows and batch size = 100  
→ You get **10 batches**

### Step 3: Loop Through Batches

- Pick **Batch 1** → Calculate Error → Update Weights  
- Pick **Batch 2** → Calculate Error → Update Weights  
- ...  
- Continue until all batches are processed

### Epoch
When **all batches are used once**, it is called **1 Epoch**.

---

## 4. Why Use Mini-Batch Gradient Descent? (Pros & Cons)

### Advantages (Pros)

- **Faster than Batch GD**  
  Weights are updated after every batch, not just once per epoch.

- **More Stable than Stochastic GD**  
  Using multiple points smooths the error compared to using only one point.

- **Memory Efficient**  
  Fits easily into RAM/GPU memory, unlike Batch GD which may load millions of rows at once.

---

### Disadvantages (Cons)

- **Extra Hyperparameter**  
  You must manually choose the **batch size**, which can be tricky.

- **Some Noise (Zigzag)**  
  It is not as perfectly smooth as Batch GD and may still show zigzag movement.

---

**Summary:**  
Mini-Batch Gradient Descent offers the **best trade-off between speed, stability, and memory usage**, which is why it is the **most commonly used gradient descent method in practice**.
