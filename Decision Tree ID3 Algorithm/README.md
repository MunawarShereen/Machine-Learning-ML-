# Decision Tree

## 1. What is a Decision Tree?

A **Decision Tree** is a **Supervised Learning algorithm**.

### Versatility
- Can be used for:
  - **Classification** (Yes / No, Spam / Not Spam)
  - **Regression** (Price, Age)
- Most commonly used for **Classification**

### Concept
- Works like a **flowchart** or a game of **“20 Questions”**
- Breaks data into smaller subsets by asking **Yes / No** questions
- Continues splitting until a final decision is reached

### Goal
To predict the value of a target variable by learning **simple decision rules** from data features.

---

## 2. Key Terms (Anatomy of a Tree)

- **Root Node**  
  The top-most node representing the entire dataset  
  This is the **best first question**

- **Splitting**  
  Dividing a node into two or more sub-nodes

- **Decision Node**  
  A node that further splits into other nodes

- **Leaf Node (Terminal Node)**  
  A node that does not split further  
  This is the **final output** (e.g., Yes / No)

---

## 3. The ID3 Algorithm

The **ID3 (Iterative Dichotomiser 3)** algorithm is a classic method for building Decision Trees.

It uses:
- **Entropy**
- **Information Gain**

###  The Big Question: How to select the Root Node?

We cannot choose any feature randomly.  
We must select the feature that best separates the data.

This is done using:

- **Entropy:** Measures impurity or randomness
- **Information Gain:** Measures how much uncertainty is reduced after a split

### Rule
The feature with the **highest Information Gain** becomes the **Root Node**.

---

## 4. Mathematical Formulas

### A. Entropy (Measure of Impurity)

Entropy tells us how mixed or messy the data is.

- 100% Yes → Entropy = 0 (Pure)
- 50% Yes / 50% No → Entropy = 1 (Maximum impurity)

#### Formula

$$
E(S) = -p_{(+)} \log_2(p_{(+)}) - p_{(-)} \log_2(p_{(-)})
$$

Where:
- \( S \): Dataset or node
- \( p_{(+)} \): Probability of positive class (Yes)
- \( p_{(-)} \): Probability of negative class (No)

---

### B. Information Gain (Measure of Value)

Information Gain answers:

> “How much cleaner does the data become after splitting using this feature?”

#### Formula

$$
\text{Gain}(S, A) = \text{Entropy}(S) -
\sum \left( \frac{|S_v|}{|S|} \times \text{Entropy}(S_v) \right)
$$

Where:
- \( \text{Gain}(S, A) \): Information Gain of feature \( A \)
- \( \text{Entropy}(S) \): Entropy of the parent dataset
- The summation term is the **weighted average entropy** of child nodes

---

## 5. Step-by-Step Example (Manual Calculation)

### Problem
Predict: **“Will I play Tennis?”**

- **Target:** Play (Yes / No)
- **Features:** Outlook, Humidity, Wind

---

### Step 1: Entropy of the Parent Dataset

Suppose:
- Total days = 14
- Yes = 9, No = 5

$$
E(\text{Parent}) =
-\frac{9}{14}\log_2\left(\frac{9}{14}\right)
-\frac{5}{14}\log_2\left(\frac{5}{14}\right)
= 0.940
$$

---

### Step 2: Entropy for Each Feature (Outlook)

Outlook splits data into:

- **Sunny:** (2 Yes, 3 No) → \( E_{sunny} \)
- **Overcast:** (4 Yes, 0 No) → \( E_{overcast} = 0 \) (Pure)
- **Rain:** (3 Yes, 2 No) → \( E_{rain} \)

#### Weighted Entropy

$$
\text{Weighted } E =
\left(\frac{5}{14} \times E_{sunny}\right)
+
\left(\frac{4}{14} \times E_{overcast}\right)
+
\left(\frac{5}{14} \times E_{rain}\right)
$$

---

### Step 3: Information Gain

$$
\text{Gain}(\text{Outlook}) =
E(\text{Parent}) - \text{Weighted } E(\text{Outlook})
$$

---

### Step 4: Compare and Select Root

After calculating gains:

- Gain(Outlook) = 0.246  
- Gain(Humidity) = 0.151  
- Gain(Wind) = 0.048  

**Winner:** Outlook → Root Node

---

### Step 5: Repeat (Recursion)

- For **Sunny**, repeat the process with remaining features
- **Overcast** is pure → Leaf Node (Stop)
- Continue until:
  - Entropy = 0, or
  - No features remain

---

## 6. Summary Checklist

- Compute Entropy of the full dataset
- For each feature:
  - Split the dataset
  - Compute entropy of each subset
  - Calculate Information Gain
- Select feature with **maximum Information Gain**
- Repeat recursively for child nodes
- Stop when a **Leaf Node** is reached
