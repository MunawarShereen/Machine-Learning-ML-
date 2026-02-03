# Random Forest Algorithm

## 1. What is Random Forest?

**Random Forest** is a powerful **Supervised Learning algorithm**.  
It is an **Ensemble Method**, specifically based on **Bagging (Bootstrap Aggregation)**, that combines multiple **Decision Trees** to create a single, robust model.

### Core Idea
> **“The wisdom of the crowd.”**

- A single Decision Tree may **overfit** or be **biased**
- A collection of many trees can **cancel out individual mistakes**

### Analogy
- **Decision Tree:** Ask one doctor for a diagnosis → they might be wrong  
- **Random Forest:** Ask 100 doctors → trust the majority opinion  

If:
- 90 doctors say *Flu*
- 10 doctors say *Cold*  

 Final decision: **Flu**

---

## 2. How Random Forest Works (The Process)

Random Forest follows a **4-step process**.

---

<img width="3058" height="1629" alt="image" src="https://github.com/user-attachments/assets/7ae243cf-96a2-4a50-82ce-a812f28f6199" />

---
### Step 1: Bootstrapping (Random Data Selection)

- The algorithm creates **multiple random datasets** from the original data
- Uses **Sampling with Replacement**
- If the original dataset has 1000 rows:
  - Each new dataset also has 1000 rows
  - Some rows may appear multiple times
  - Some rows may not appear at all

**Result:**  
Each tree sees a **slightly different version** of the data.

---

### Step 2: Random Feature Selection

This is the **“Random”** part of Random Forest.

- In a normal Decision Tree:
  - All features are considered at each split
- In Random Forest:
  - Only a **random subset of features** is considered at each node  
  - Example: 3 out of 10 columns

#### Why do this?
- Forces trees to be **different (diverse)**
- Prevents one strong feature from dominating all trees
- Reduces correlation between trees

---

### Step 3: Building the Trees

- A **full Decision Tree** is trained for each random dataset
- Trees are **independent** of each other
- Example:
  - `n_estimators = 100`
  - 100 separate Decision Trees are built

---

### Step 4: Aggregation (Final Decision)

Once all trees are trained, new data is passed to **every tree**.

#### For Classification (Majority Voting)
- Tree 1 → Yes
- Tree 2 → No
- Tree 3 → Yes


**Final Output:** Yes (majority wins)

---

#### For Regression (Averaging)
- Tree 1 → 50
- Tree 2 → 60
- Tree 3 → 55

  
$$
\text{Final Prediction} = \frac{50 + 60 + 55}{3} = 55
$$

---

## 3. Why Use Random Forest? (Benefits)

- **Reduced Overfitting**  
  Averages results of many trees, canceling individual errors

- **High Accuracy**  
  One of the best-performing algorithms for **tabular data**

- **Handles Missing Values**  
  Maintains good performance even when data is incomplete

---

## 4. Key Hyperparameters

Important parameters you can tune in code:

- **`n_estimators`**  
  Number of trees in the forest (e.g., 100)

- **`max_features`**  
  Number of features considered at each split

- **`bootstrap`**  
  Whether to use sampling with replacement (`True` / `False`)

---

## 5. Summary Formulas

### Classification

$$
\text{Final Prediction}=\text{Mode}(\text{Tree}_1, \text{Tree}_2, \dots, \text{Tree}_n)
$$

---

### Regression

$$
\text{Final Prediction}=\text{Mean}(\text{Tree}_1, \text{Tree}_2, \dots, \text{Tree}_n)
$$

---

### ✅ Final Takeaway
Random Forest is **robust, accurate, and reliable** because it relies on **many weak learners** instead of one strong but risky model.


