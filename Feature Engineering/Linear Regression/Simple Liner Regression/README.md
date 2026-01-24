## Simple Linear Regression

### 1. What is Simple Linear Regression?

**Simple Linear Regression (SLR)** is a supervised machine learning algorithm used to model the relationship between **one independent variable (X)** and **one dependent variable (Y)** using a straight line.

It answers questions like:
- How does **Y** change when **X** changes?
- Can we predict **Y** for a new value of **X**?

---

### 2. Mathematical Equation

The equation of Simple Linear Regression is:

\[
y = mx + b
\]

Where:
- **y** → Predicted output (dependent variable)
- **x** → Input feature (independent variable)
- **m** → Slope (how much y changes when x increases by 1)
- **b** → Intercept (value of y when x = 0)

---

### 3. Intuition Behind the Line

The algorithm tries to draw a **best-fit straight line** through the data points such that the **total error is minimized**.

- If **m > 0** → Positive relationship (as X increases, Y increases)
- If **m < 0** → Negative relationship (as X increases, Y decreases)
- If **m = 0** → No relationship

---

### 4. How Does the Model Learn?

The model learns by minimizing a cost function called **Mean Squared Error (MSE)**:

\[
MSE = \frac{1}{n} \sum (y_{actual} - y_{predicted})^2
\]

This is usually done using:
- **Gradient Descent**, or
- **Normal Equation**

The goal is to find the best values of **m** and **b**.

---

### 5. Assumptions of Simple Linear Regression

For the model to work well, these assumptions should approximately hold:

1. **Linearity:** Relationship between X and Y is linear  
2. **Independence:** Observations are independent  
3. **Homoscedasticity:** Constant variance of errors  
4. **Normality:** Errors are normally distributed  
5. **No Outliers:** Extreme values can heavily affect the line  

---

### 6. Example

**Problem:** Predict Salary based on Years of Experience.

- X = Years of Experience  
- Y = Salary  

If the model learns:
\[
y = 5000x + 20000
\]

Then for **5 years of experience**:
\[
Salary = 5000(5) + 20000 = 45000
\]

---

### 7. Advantages

- Simple and easy to understand  
- Fast to train  
- Highly interpretable  
- Works well for linear relationships  

---

### 8. Limitations

- Cannot handle complex (non-linear) patterns  
- Very sensitive to outliers  
- Works only with one input feature  

---

### 9. When to Use Simple Linear Regression?

- When you have **one input feature**
- When the relationship looks **roughly linear**
- When interpretability is important

---
