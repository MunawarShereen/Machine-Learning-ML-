## Handling Categorical Features

### 1. Why do we need this?

Machine Learning models (such as **Linear Regression** and **SVM**) are purely mathematical.  
They **only understand numbers** (`1, 2, 3, ...`) and **cannot understand text or strings** like `"Red"`, `"Blue"`, `"Good"`, or `"Bad"`.

**Handling Categorical Features** is the process of converting these text-based categories into numerical values so that Machine Learning models can process them correctly.

---

## 2. Types of Categorical Data

Before encoding, it is very important to identify **which type of categorical data** you are dealing with.

---

### A. Nominal Data

#### Definition
Categories that **do not have any mathematical order or ranking**.

#### Examples
- **Colors:** Red, Blue, Green  
  (Red is not greater or smaller than Blue)
- **States:** Sindh, Punjab, Balochistan
- **Gender:** Male, Female

#### Technique Used
- **One Hot Encoding**

---

### B. Ordinal Data

#### Definition
Categories that **have a clear order or ranking**.

#### Examples
- **Education:** School < College < University
- **Reviews:** Bad < Average < Good
- **T-Shirt Size:** S < M < L < XL

#### Technique Used
- **Ordinal Encoding**
- **Label Encoding** (in some cases)

---

## 3. Encoding Techniques

### A. Ordinal Encoding

#### When to use
- When **input features (X)** are **ordinal** (have a meaningful order).

#### How it works
- Assigns integers based on rank or order.

**Example:**
- Small → 1  
- Medium → 2  
- Large → 3  

#### Library Used
- `OrdinalEncoder` from **sklearn**

### B. Label Encoding

#### When to use
- **STRICTLY** for the **target variable (y)**
- ❌ **Do NOT use** for input features (X)

#### How it works
- Automatically converts class labels into numerical values  
  `(0, 1, 2, ...)`

#### Library Used
- `LabelEncoder` from **sklearn**

---

### C. One Hot Encoding (OHE)

#### When to use
- When **input features (X)** are **nominal**
- No natural order exists between categories

#### How it works
- Creates a **separate column for each category**
- Values are binary: `0` or `1`

#### Example
If a column **Color** contains:

- Red
- Green
- Blue

OHE will create the following columns:

- `Color_Red`
- `Color_Green`
- `Color_Blue`

If a row has **Red**, then:

- `Color_Red = 1`
- `Color_Green = 0`
- `Color_Blue = 0`

---

## ⚠️ Dummy Variable Trap

### Problem
If we create a dummy column for **every category**, the features become highly correlated.  
This problem is called **Multicollinearity**, which can confuse Machine Learning models.

#### Example
If:
- `Red = 0`
- `Blue = 0`

Then **Green MUST be 1** automatically.  
So the **Green** column becomes unnecessary.

---

### Solution: n − 1 Rule

- If a feature has **n categories**, create only **n − 1 columns**
- Drop one category to avoid multicollinearity

#### Example
For **Red, Green, Blue** (3 categories):

- Create only **2 columns**: `Red`, `Blue`

If:
- `Red = 0`
- `Blue = 0`

The model automatically understands that the value is **Green**


