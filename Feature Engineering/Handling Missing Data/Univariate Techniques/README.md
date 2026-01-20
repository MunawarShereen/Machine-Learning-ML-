# Univariate Imputation Techniques (Numerical)

These techniques are used when we consider **only one column** to fill its missing values.

---

## 1. Mean / Median Imputation

**When to use:**  
When data is **Missing Completely At Random (MCAR)** — missing by accident.

#### The Rule
- **Use Mean:** When the data follows a **Normal Distribution** (Bell Curve)
- **Use Median:** When the data is **Skewed** or contains **outliers**

#### Pros and Cons
**Advantages**
- Very simple and fast to apply

**Disadvantages**
- Changes the original distribution
- Can introduce **artificial (fake) outliers**

---

## 2. Arbitrary Value Imputation

**When to use:**  
When data is **Missing Not At Random (MNAR)**.

**How it works:**  
Replace missing values with a fixed number such as `0`, `999`, or `-1`.

**Why this works:**  
It explicitly signals the model that the value was missing, which may carry important information.

#### Pros and Cons
**Advantages**
- Easy to implement
- Captures the importance of missingness

**Disadvantages**
- Alters **variance** and **covariance**
- Can negatively affect relationships between features

---

## 3. End of Distribution Imputation

**When to use:**  
MNAR — this is an extension of Arbitrary Value Imputation.

**How it works:**  
Instead of using a random number like `999`, you calculate an extreme value at the end of the distribution.

**Example:**  
`Mean + 3 × Standard Deviation`

#### Pros and Cons
**Advantages**
- Keeps missing values clearly separated from real values

**Disadvantages**
- Distorts the shape of the distribution

---

## 4. Random Sample Imputation

**How it works:**  
Randomly selects a real value from the existing (non-missing) data in the same column and uses it to fill the missing value.

#### Pros and Cons
**Advantages**
- Preserves **mean**, **variance**, and **distribution shape**
- More realistic than mean/median imputation

**Disadvantages**
- Memory intensive
- Requires storing the original training data for production use

---

## 5. Missing Indicator

**How it works:**  
Before imputing values, create a **new binary column** (e.g., `Age_NA`):

- `True` → Value was missing  
- `False` → Value was present

**Purpose:**  
Allows the model to learn that **missingness itself is a pattern**.

---

# Handling Missing Categorical Data

---

## 1. Most Frequent Imputation (Mode)

**How it works:**  
Replace missing values with the **most frequent category** in the column.

**When to use:**  
When data is **MCAR**.

#### Pros and Cons
**Advantage**
- Very easy and fast

**Disadvantage**
- Can over-represent the dominant category if many values are missing

---

## 2. New Category Imputation

**How it works:**  
Treat missing values as a **separate category** by replacing `NaN` with labels like `"Missing"` or `"Unknown"`.

**When to use:**  
When data is **MNAR**.

#### Pros
 No data loss  
 Helps the model learn the importance of missingness

---
