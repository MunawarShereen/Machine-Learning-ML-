## Outliers

### 1. What is an Outlier?

An **Outlier** is a data point that is very different from the rest of the data.  
It stands out like a **“black sheep”** in a flock of white sheep.

**Example:**  
Imagine you are collecting the ages of people in a survey:
20, 25, 30, 22, 28, 300


The value **300** is an outlier because it is impossible for a human to live that long.

---

### 2. When Are Outliers Dangerous vs. Helpful?

#### When Are They Dangerous? (Bad)

Outliers are dangerous when they are **errors or garbage data**.  
They can seriously confuse Machine Learning models.

**Affected Algorithms:**  
Algorithms that rely on **weights and distances** are highly sensitive to outliers:

- Linear Regression  
- Logistic Regression  
- Deep Learning (Neural Networks)  
- K-Means Clustering  

An outlier can pull the model strongly toward itself and distort predictions.

---

#### When Are They Helpful? (Good)

Sometimes, outliers are exactly what we want to find.

**Anomaly Detection Examples:**

- **Credit Card Fraud:**  
  If you usually spend \$10 and suddenly spend \$10,000, that outlier helps detect fraud.

- **Factory Defect:**  
  If 99 screws are 5 cm long and one screw is 2 cm, that outlier signals a machine issue.

---

### 3. How to Detect Outliers?

There are three common methods to detect outliers.

#### A. Z-Score Method

**Requirement:** Data must follow a **Normal Distribution (Bell Curve)**.

**Rule:**  
In a normal distribution:
- 68% of data lies near the mean  
- 99.7% of data lies within **±3 standard deviations (3σ)**

Anything outside this range is an outlier.

**Formulas:**

- **Upper Limit:**  
  \[
  \text{Mean} + 3 \times \text{Standard Deviation}
  \]

- **Lower Limit:**  
  \[
  \text{Mean} - 3 \times \text{Standard Deviation}
  \]

---

#### B. IQR Method (Interquartile Range)

**Requirement:** Used when data is **skewed** (not normally distributed).

**Concept:**

- **Q1:** 25th percentile  
- **Q3:** 75th percentile  
- **IQR:** Middle 50% of data  
  \[
  \text{IQR} = Q3 - Q1
  \]

**Rule:**

- **Minimum Limit:**  
  \[
  Q1 - 1.5 \times \text{IQR}
  \]

- **Maximum Limit:**  
  \[
  Q3 + 1.5 \times \text{IQR}
  \]

Any value outside these limits is an outlier.

---

#### C. Percentile Method

**Concept:**  
A percentile shows what percentage of values are below a given point.

**Example:**  
If you are in the **99th percentile**, you performed better than 99% of people.

**Rule:**  
You manually set limits:
- Bottom **1%** (below 1st percentile)
- Top **1%** (above 99th percentile)

Values outside these ranges are treated as outliers.

---

### 4. How to Treat Outliers?

Once outliers are identified, there are two main approaches.

#### 1. Trimming (Deletion)

**What is it?**  
Completely remove rows containing outliers.

**When to use:**  
- Dataset is large  
- Outliers are very few

**Risk:**  
- Reduces dataset size  
- Potential loss of information

---

#### 2. Capping (Winsorization)

**What is it?**  
Replace outliers with the nearest allowed limit instead of deleting them.

**Example:**
- Max limit = 80, value = 300 → change `300 → 80`
- Min limit = 5, value = 1 → change `1 → 5`

**Benefit:**  
- Keeps the data row  
- Prevents outliers from harming the model

---
