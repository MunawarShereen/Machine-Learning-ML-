## Handling Missing Data

### 1. What is Missing Data?

In real-world datasets, information is often lost or not recorded. These empty cells are called **Missing Values**, usually represented as **NaN** or **Null**.

When you encounter missing data, there are **two main approaches** to handle it:

---

### Option A: Removal (Deletion)

**What it is:**  
You simply delete the rows that contain missing values.

**When to use:**  
- When you have a **large dataset**
- When the missing portion is **very small (less than 5%)**

**Downside:**  
- You may lose important and useful information.

---

### Option B: Imputation (Filling)

**What it is:**  
You fill the missing values with an estimated or calculated value instead of deleting the data.

#### Types of Imputation

**1. Univariate Imputation**  
- Uses information from **only one column**.
- **Example:** Filling missing values in the `Age` column using the **mean (average)** age.

**2. Multivariate Imputation**  
- Uses information from **multiple related columns**.
- **Example:** If `Weight` is missing, you use `Height` and `Gender` to predict and fill the missing value more accurately.

---

##  Complete Case Analysis (CCA)

### 1. What is CCA?

**Complete Case Analysis (CCA)**, also known as **List-wise Deletion**, is the simplest method for handling missing data.

**Definition:**  
Any row that contains **at least one missing value** is completely removed from the dataset.

**Why this name?**  
Because only **“complete cases”** (rows with no missing values) are kept.

---

### 2. Assumptions (When should you use it?)

You should only apply CCA when the following conditions are met:

- **Missing Completely At Random (MCAR):**  
  The missing data has no pattern and occurs purely by chance.

- **Small Amount of Missing Data:**  
  Ideally, less than **5%** of the dataset should be missing.

---

### 3. Pros and Cons

#### Pros
- Very easy to implement
- No complex calculations required
- Preserves the original data distribution (if data is MCAR)

#### Cons
- **Data Loss:** Large portions of the dataset may be deleted
- **Bias Risk:**  
  If data is not missing at random (e.g., high-income individuals refusing to disclose income), deleting rows can introduce bias into the model

---
