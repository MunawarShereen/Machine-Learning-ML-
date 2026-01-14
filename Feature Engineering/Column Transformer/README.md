## Column Transformer

### 1. What is Column Transformer?

In a real-world dataset, we usually have **different types of columns**, and each type requires a different kind of preprocessing:

- **Numerical Columns** (e.g., Age, Salary)  
  → Require **Scaling** or **Imputation** (filling missing values)

- **Categorical Columns** (e.g., City, Gender)  
  → Require **Encoding** (One-Hot Encoding or Ordinal Encoding)

Traditionally, these preprocessing steps are applied **separately**, and the transformed data is then manually combined. This approach can become **messy, repetitive, and hard to manage**.

**Column Transformer** is a utility in **Scikit-Learn** that allows you to apply **different transformations to different columns at the same time**, all within a **single block of code**.

---

### Real-World Analogy

Think of a **car wash station**:

- Tyres get **polished**
- Glass gets **cleaned**
- Car body gets **waxed**

Each part of the car receives a **different treatment**, but everything happens **simultaneously**.

**Column Transformer** works the same way by applying the right transformation to the right columns at once.

---

### 2. Why do we need it?

- **Clean Code**  
  No need to write separate preprocessing logic for each column type and then merge everything manually.

- **Easy Pipelines**  
  Makes it simple to build end-to-end **Machine Learning Pipelines**.

- **Safety & Reliability**  
  Reduces the chances of mistakes, such as forgetting to transform a column or applying the wrong transformation.

