# Stochastic Gradient Descent (SGD)

## 1. Why Do We Need SGD? (Problems with Batch Gradient Descent)

Batch Gradient Descent works well for small datasets, but it becomes impractical when the data size grows very large.

### Scenario

Imagine a dataset with:
- **Rows ($n$):** 1,000,000 (1 million)
- **Columns:** 5
- **Epochs:** 50

### Problems

- **Slow Speed**  
  To update the weights just once, the algorithm must calculate the error for all **1,000,000 rows**.  
  Over **50 epochs**, this becomes **50 million calculations**, which is extremely slow.

- **Hardware / RAM Crash**  
  Batch GD tries to load the **entire dataset into RAM** to compute the gradient.  
  If your system has **8 GB RAM** but the dataset is **50 GB**, the system may freeze or crash.

---

## 2. How Does SGD Solve This?

The word **“Stochastic”** means **Random**.

Instead of using the entire dataset, SGD works very differently:

- **Batch Gradient Descent**  
  Uses **all rows** → Calculates total error → Updates weights **once**

- **Stochastic Gradient Descent**  
  Picks **one random row** → Calculates error → Updates weights **immediately**

### Result

- **Faster Learning**  
  The model starts learning right after seeing the **first row**.

- **Low Memory Usage**  
  Only one row is loaded into RAM at a time, allowing training on **huge datasets**, even on low-end machines.

---

## 3. The Path: Zigzag vs. Straight

Because SGD updates weights using **only one random row**, the updates are noisy.

- **Batch Gradient Descent**  
  Follows a **smooth, straight path** toward the minimum.

- **Stochastic Gradient Descent**  
  Follows a **zigzag (fluctuating) path**.  
  One data point may suggest moving left, another suggests moving right.

### The Issue

SGD does not settle exactly at the global minimum.  
It keeps **oscillating around the bottom** of the valley.

---

## 4. The Solution: Learning Rate Schedules

To reduce the zigzag behavior near the solution, we use a **Learning Rate Schedule**.

### Idea

- **Start with a High Learning Rate**  
  Large steps help the model learn quickly at the beginning.

- **Gradually Reduce the Learning Rate**  
  Smaller steps near the solution help the model settle down.

This prevents overshooting the minimum and improves convergence.

---

## 5. When Should You Use SGD?

You should prefer **Stochastic Gradient Descent** when:

- **Big Data**  
  When the dataset contains **millions of rows** and Batch GD is too slow.

- **Non-Convex Loss Functions**  
  When the loss surface has many **local minima**.

Because SGD is random and noisy, it has enough energy to:
- Escape local minima
- Reach the **global minimum** more effectively

---

**Summary:**  
Stochastic Gradient Descent is **fast, memory-efficient, and scalable**, making it ideal for **very large datasets**, though it requires careful tuning of the learning rate to control noise.
