# Naive Bayes Algorithm

## 1. What is Naive Bayes?

Naive Bayes is a **Supervised Machine Learning** algorithm used for **classification tasks** such as spam filtering and sentiment analysis.  
It is based on **Bayes’ Theorem** from probability theory.

### Why is it called *“Naive”*?

It makes a **naive (simple) assumption**: all features are **independent** of each other.

**Example:**  
If a fruit is **Red**, **Round**, and **3 inches** in diameter, Naive Bayes assumes that:
- “Red” is independent of “Round”
- “Round” is independent of “3 inches”

In real life, features are often related, but this assumption makes the algorithm:
- **Very fast**
- **Surprisingly accurate** in many real-world problems

---

## 2. The Formula (Bayes’ Theorem)

Bayes’ Theorem is written as:

$$
P(C \mid X) = \frac{P(X \mid C)\, P(C)}{P(X)}
$$

Where:

- **$P(C \mid X)$ — Posterior**  
  Probability of class \(C\) given the features \(X\)

- **$P(X \mid C)$ — Likelihood**  
  Probability of observing features \(X\) given class \(C\)

- **$P(C)$ — Prior**  
  Initial probability of class \(C\) (before seeing any data)

- **$P(X)$ — Evidence**  
  Total probability of observing the features \(X\)

---

## 3. Types of Naive Bayes Classifiers

Different types of data require different Naive Bayes variants.

### A. Bernoulli Naive Bayes

- **Best used for:** **Binary / Boolean features** (True/False, 0/1, Yes/No)
- **Example:** **Spam Detection**

Key idea:
- We do **not** care how many times a word appears
- We only care **whether it appears or not**

**Example:**
- Word “Free” → Present? **Yes / No**

**Logic:**
- Considers both:
  - Feature presence
  - Feature absence  
- Explicitly penalizes missing features

---

### B. Multinomial Naive Bayes

- **Best used for:** **Discrete count / frequency data**
- **Example:** **Document classification (News vs Sports)**

Key idea:
- **Frequency matters**

**Example:**
- Word “Goal” appears:
  - 10 times → very strong signal for *Sports*
  - 1 time → weaker signal

**Logic:**
- Uses word counts to calculate probabilities

---

### C. Gaussian Naive Bayes

- **Best used for:** **Continuous / real-valued data**
- **Example:** **Iris Flower Dataset**

Features look like:
- `Sepal Length = 5.1 cm`
- `Petal Width = 0.4 cm`

**Logic:**
- Since continuous values rarely repeat, we assume the data follows a  
  **Normal Distribution (Bell Curve)**
- Probability is calculated using:
  - **Mean (μ)**
  - **Standard Deviation (σ)**

**Gaussian Probability Formula:**

$$
P(x \mid C) =
\frac{1}{\sqrt{2\pi\sigma^2}}
\exp\left(-\frac{(x - \mu)^2}{2\sigma^2}\right)
$$

> You do **not** need to memorize this formula — just remember it uses **mean** and **standard deviation**.

---

## 4. Summary Comparison

| Type | **Bernoulli NB** | **Multinomial NB** | **Gaussian NB** |
|-----|-----------------|--------------------|-----------------|
| **Data Type** | Binary (0/1) | Discrete counts (1, 5, 10…) | Continuous (1.5, 3.2…) |
| **Feature Focus** | Presence vs Absence | Frequency / Count | Distribution (Bell Curve) |
| **Key Example** | Spam Detection | Text Classification | Iris / Health Data |

---

## 5. Simple Example

**Task:** Predict whether a review is **Positive (1)** or **Negative (0)**

**Review:**  
> “Love this movie”

### 1. Bernoulli Naive Bayes
- “Love” present? → **Yes**
- “Movie” present? → **Yes**
- “Hate” present? → **No**

(Absence also matters)

---

### 2. Multinomial Naive Bayes
- “Love” → count = 1
- “Movie” → count = 1

Uses these counts to compute probabilities.

---

### 3. Gaussian Naive Bayes
- **Not applicable** here  
- Text is not continuous numerical data like 3.5 or 7.2

- Spam filtering
- High-dimensional data
