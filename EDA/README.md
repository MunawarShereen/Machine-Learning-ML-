# Exploratory Data Analysis (EDA)

EDA stands for Exploratory Data Analysis. Think of it like "interviewing" your data. Before building any machine learning model, it is important to explore the data to understand what it contains. EDA helps identify patterns, detect errors, and validate assumptions.

**Simple Example:**  
If you are cooking a new dish, checking all your ingredients before cooking is similar to performing EDA.

---

## 1. Univariate Analysis

Univariate analysis focuses on analyzing **one variable at a time**. The goal is to understand the distribution and characteristics of a single column without considering relationships with other columns.

### A. Numerical Column (Histogram / Distribution)

When a column contains numerical values (such as Age, Price, or Marks), we analyze its distribution to see which values are most common.

**Example:**  
In the Titanic dataset (`train.csv`), analyzing the **Age** column.

**Observation:**  
Most passengers were between **20 and 30 years old**.

---

### B. Categorical Column (Countplot)

For categorical columns (such as Yes/No, Male/Female), we count how many times each category appears.

**Example:**  
In the Titanic dataset, counting how many passengers **Survived**  
(0 = Died, 1 = Survived).

**Observation:**  
More passengers **died (0)** than **survived (1)**.

---

## 2. Multivariate Analysis

Multivariate analysis examines **relationships between two or more variables**. This helps us understand how different features interact with each other.

### A. Scatterplot (Numerical - Numerical)

Scatterplots are used when comparing two numerical variables to identify correlation or trends.

**Use Case:**  
Check if higher CGPA leads to higher IQ.

**Hue:**  
`hue='placement'` is used to color points based on placement status.

**Example:**  
CGPA vs IQ from `placement.csv`.

**Observation:**  
Students with higher CGPA and IQ (top-right area) are more likely to be placed.

---

### B. BarPlot (Numerical - Categorical)

Barplots compare a numerical value across different categories, usually using the mean.

**Use Case:**  
Compare average **Fare** for different **Passenger Classes (Pclass)**.

**Hue:**  
`hue='Sex'` separates bars by gender.

**Example:**  
Pclass vs Fare from `train.csv`.

**Observation:**  
- First Class tickets are much more expensive than Second or Third Class.  
- In First Class, females paid more on average than males.

---

### C. Distplot / KDE Plot (Numerical - Categorical)

Distplots or KDE plots show the shape of data distribution. Using a categorical column as hue allows comparison between groups.

**Use Case:**  
Compare age distribution of passengers who **Survived** vs **Died**.

**Hue:**  
`hue='Survived'`.

**Example:**  
Age distribution by Survived from `train.csv`.

**Observation:**  
- Children (age 0–5) had higher survival chances.  
- Many young adults (20–30) did not survive.

---

### D. ClusterMap / Heatmap (Categorical - Categorical)

When working with two categorical variables, heatmaps show frequency using color intensity.

**Use Case:**  
Analyze survival counts across different passenger classes.

**Explanation:**  
Darker colors indicate higher values. Clustermaps group similar rows and columns together.

**Example:**  
Pclass vs Survived from `train.csv`.

**Observation:**  
- Most casualties were from **3rd Class**.  
- **1st Class** had a higher survival rate compared to deaths.
