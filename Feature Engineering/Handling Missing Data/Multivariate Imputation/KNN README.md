## KNN (K-Nearest Neighbors)

### 1. What is KNN?

**KNN (K-Nearest Neighbors)** is a simple Machine Learning algorithm used for both:

- **Classification** (predicting categories)
- **Regression** (predicting numerical values)

**Core Concept:**  
It follows the proverb:  
> *“Tell me who your friends are, and I will tell you who you are.”*

**Intuition:**  
If a new data point appears near **5 Red points** and **1 Blue point**, the algorithm assumes the new point is **Red**.

---

### 2. How KNN Works (Step-by-Step)

#### Step 1: Choose K
- **K** is the number of nearest neighbors to consider.
- If `K = 3`, look at the **3 closest points**.
- If `K = 5`, look at the **5 closest points**.

---

#### Step 2: Calculate Distance (Euclidean Distance)

To find the nearest neighbors, we calculate how far the new point is from all other points.

**Euclidean Distance Formula:**

\[
d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
\]

This is like measuring the straight-line distance using a ruler.

**Handling Missing Values (NaN):**  
Advanced implementations (e.g., `nan_euclidean_distances`) can handle missing values by:
- Ignoring missing coordinates
- Re-weighting remaining values so the distance remains fair

---

#### Step 3: Make a Decision

Once the **K nearest neighbors** are found, the decision depends on the task type:

##### A. Classification (Categories)
- **Logic:** Majority Voting (Mode)
- **Example:**  
  - `K = 3`
  - Neighbors = `[Cat, Cat, Dog]`  
  - **Result:** `Cat` (majority wins)

##### B. Regression (Numbers)
- **Logic:** Average (Mean)
- **Example:**  
  - Neighbor house prices = `[100k, 120k, 110k]`  
  - **Result:**  
    \[
    (100 + 120 + 110) / 3 = 110k
    \]

---

### 3. Weighted KNN

In standard KNN, **all neighbors are treated equally**.  
However, closer neighbors should usually have **more influence**.

**Weighted Distance Formula:**

\[
\text{Weight} = \frac{1}{\text{Distance}}
\]

- **Closer points → Higher weight**
- **Farther points → Lower weight**

This improves prediction accuracy when distances vary significantly.

---

### 4. Advantages & Disadvantages

#### Advantages (Pros)
- **Simple:** Easy to understand and explain
- **Accurate:** Works well on small datasets
- **No Assumptions:** Does not assume any data distribution

#### Disadvantages (Cons)
- **Slow:** A *lazy learner* — no training phase, calculates distance every time
- **Memory Heavy:** Stores the entire training dataset in memory
- **Sensitive to Scale:**  
  Feature Scaling (e.g., `StandardScaler`) is **mandatory** if features have different ranges

---
