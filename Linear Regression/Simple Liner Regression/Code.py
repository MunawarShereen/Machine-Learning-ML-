import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 1. Load the Dataset
# We read the 'dataset path.csv' file and store it in a DataFrame called 'df'.
df = pd.read_csv('placement.cs')

# 2. Visualize the Data
# We draw a Scatter Plot to see the relationship between CGPA and Package.
# This is important to check if the data follows a linear pattern (straight line).
plt.scatter(df['cgpa'], df['package'])
plt.xlabel('CGPA')              # Label for x-axis
plt.ylabel('Package(in lpa)')   # Label for y-axis
plt.show()                      # Displays the graph

# 3. Separate Input (X) and Output (y)
# X = Independent Variable (Feature). We need a 2D array for sklearn, so we use iloc[:, 0:1].
# This selects all rows (:) and the first column (0:1).
X = df.iloc[:, 0:1]

# y = Dependent Variable (Target). This is what we want to predict.
# This selects all rows (:) and the last column (-1).
y = df.iloc[:, -1]

# 4. Train-Test Split
# We split the data into two parts:
# - Train Data (80%): Used to teach the model.
# - Test Data (20%): Used to check if the model is correct.
# random_state=2 ensures that the data is split in the exact same way every time you run the code.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

# 5. Create the Model
# We create an object 'lr' of the LinearRegression class.
lr = LinearRegression()

# 6. Train the Model
# The .fit() function is the heart of ML. It is where the learning happens.
# The model looks at X_train (CGPA) and y_train (Package) and calculates the best line (m and b).
lr.fit(X_train, y_train)

# 7. Make a Prediction
# We pick the first student from the Test Data (X_test.iloc[0]).
# .values extracts the number.
# .reshape(1,1) converts it from a scalar (e.g., 7.5) to a 2D array [[7.5]].
# Scikit-Learn ALWAYS expects a 2D array for input, even for a single prediction.
predicted_package = lr.predict(X_test.iloc[0].values.reshape(1,1))

print("Predicted Package:", predicted_package)
