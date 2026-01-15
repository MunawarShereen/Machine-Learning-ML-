## Handling Mixed Variables

### 1. What are Mixed Variables?

**Mixed variables** are columns in a dataset that contain both **numerical values** and **categorical values (text)**. This situation commonly occurs in real-world data and usually appears in two forms:

---

#### Scenario A: Mixed Rows

In this case, different rows within the same column contain different data types.

- Some rows contain **numbers** (e.g., `123`)
- Other rows contain **text** (e.g., `ABC`)

---

#### Scenario B: Mixed Values in One Cell

In this case, a single cell contains **both letters and numbers combined**.

- Examples: `C85`, `B123`, `A5`

---

Machine Learning models **cannot directly process mixed data types** in a single column.  
To handle this, we split the column into **two separate columns**:

- One column for the **numerical part**
- One column for the **categorical part**

---

## 2. Techniques to Handle Mixed Variables

### A. Scenario 1: Numerical & Categorical in Different Rows

#### Problem
Some rows contain numbers (e.g., `12`), while others contain text (e.g., `Hello`) in the same column.

#### Solution
Create **two new columns**:

- **Numerical Column:**  
  Convert all values to numbers. Non-numeric values are converted to `NaN`.

- **Categorical Column:**  
  Identify rows where numerical conversion failed (`NaN`) and store the original text values there.

---

### B. Scenario 2: Numerical & Categorical Combined in One Cell

#### Problem
Values appear as a combination of letters and numbers, such as `C85`, `D12`, or `A5`.

#### Solution
**Parse the string** to separate components:

- **Numerical Part:** Extract the digits (`85`, `12`, `5`)
- **Categorical Part:** Extract the letter(s) (`C`, `D`, `A`)

---

### Code Logic
- Use string operations or regular expressions
- Separate alphabets and numbers into different columns
- Apply further preprocessing (encoding, scaling) as needed

