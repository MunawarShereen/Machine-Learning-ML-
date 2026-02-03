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

