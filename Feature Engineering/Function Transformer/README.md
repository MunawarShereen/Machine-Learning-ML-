## Function Transformer

### 1. What is Function Transformer?

In Machine Learning, many algorithms (such as **Linear Regression** and **Logistic Regression**) perform better when the input data follows a **Normal Distribution (Bell Curve)**.

However, real-world data is often **skewed**, meaning it is tilted toward one side.

A **Function Transformer** is a preprocessing technique used to **change the shape of a data distribution**. It applies a mathematical function (such as **Log**, **Square**, **Reciprocal**, or **Square Root**) to every value in a column to make the data more **Normal (Gaussian)**.

---

### 2. Types of Transformations

#### A. Log Transformer (`log(x)`)

**Use Case:**  
- Best suited for **Right-Skewed data** (long tail on the right side)

**How it works:**  
- Compresses large values heavily  
- Pulls the long tail back toward the center of the distribution

**Limitation:**  
- Cannot be applied to **zero or negative values**  
- `log(0)` and `log(-1)` are undefined

---

#### B. Square Transformer (`x²`)

**Use Case:**  
- Best for **Left-Skewed data** (long tail on the left side)

**How it works:**  
- Squaring small values keeps them small  
- Squaring large values makes them much larger  
- This stretches the right side and helps correct left skewness

---

#### C. Reciprocal Transformer (`1 / x`)

**Use Case:**  
- Also used for **Right-Skewed data**

**How it works:**  
- Has a very strong transformation effect  
- Reverses the order of values (small becomes large, large becomes small)

**Limitation:**  
- Cannot be applied when the value is **0**

---

#### D. Square Root Transformer (`√x`)

**Use Case:**  
- Suitable for **Right-Skewed data**, but less aggressive than Log transformation

**Benefits:**  
- Can be applied to **zero values**, unlike the Log transformer

---

### 3. How to Check if Data is Normal?

To verify whether data follows a normal distribution, we commonly use:

- **Distplot (Histogram):**  
  Helps visually inspect whether the data resembles a bell-shaped curve.

- **QQ Plot (Quantile-Quantile Plot):**  
  A diagnostic plot where, if the points lie close to the diagonal red line, the data is considered normally distributed.

