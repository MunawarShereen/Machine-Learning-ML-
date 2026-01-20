## 1. What is MICE?

**MICE** stands for **Multivariate Imputation by Chained Equations**.  
It is a **“smart” imputation technique** that predicts missing values using **all other columns** in the dataset, unlike simple methods (Mean/Median) which look at only one column.

**When to use:**  
- When data is **Missing At Random (MAR)**

**Assumption:**  
- There is a relationship between columns (e.g., `Age` is related to `Salary`)

---

## 2. How the MICE Algorithm Works (Step-by-Step)

Imagine a dataset with three columns: `Age`, `Salary`, `Tax`. Some values are missing in all of them.

---

### Step 0: Initial Filling (Iteration 0)

- Fill **all missing values** in every column with the **Mean** of that column.
- The dataset is now complete, but these values are **just rough guesses**.

---

### Step 1: The “Chained” Prediction (Iteration 1)

Refine the guesses **one column at a time (Left to Right)**:

#### Column 1: Age
- Delete the previously guessed values in `Age` (make them missing again)
- **Input Features (X):** Salary, Tax  
- **Target (y):** Age  
- Train a **Linear Regression** model to predict missing `Age` values
- Replace missing `Age` with the predicted values

#### Column 2: Salary
- Delete the previously guessed values in `Salary`  
- **Input Features (X):** Age (new predicted) and Tax  
- **Target (y):** Salary  
- Train a model and fill missing `Salary` values

#### Column 3: Tax
- Repeat the same process using the latest `Age` and `Salary` predictions as features

---

### Step 2: Repeat (Iteration 2, 3, …)

- Repeat the **entire cycle multiple times**
- In each iteration, the model uses **improved values** from the previous iteration to make **more accurate predictions**

---

### Step 3: Stop (Convergence)

- Stop when the predictions **stop changing** significantly

**Formula:**  

\[
\text{Difference} = \text{Iteration\_Current} - \text{Iteration\_Previous}
\]

- If the difference is **0** (or very close), the model has **converged** and found the best imputed values
