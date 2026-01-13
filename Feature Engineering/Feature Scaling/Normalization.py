import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler  # <--- Import this

# 1. Load Data
df = pd.read_csv('YourDatasetPath.csv')
df = df.iloc[:,2:] # Taking only Age and EstimatedSalary

# 2. Split Data
x_train, x_test, y_train, y_test = train_test_split(
    df.drop("Purchased", axis=1),
    df['Purchased'],
    test_size=0.3,
    random_state=0
)

# 3. Apply Normalization (MinMaxScaler)
scaler = MinMaxScaler()

# fit the scaler to the train set, it will learn the Min and Max values
scaler.fit(x_train)

# transform train and test sets
x_train_scaled = scaler.transform(x_train)
x_test_scaled = scaler.transform(x_test)

# 4. Convert back to DataFrame for easy viewing
x_train_scaled = pd.DataFrame(x_train_scaled, columns=x_train.columns)
x_test_scaled = pd.DataFrame(x_test_scaled, columns=x_test.columns)

# 5. Check the Description
# You will see Min is 0.0 and Max is 1.0
print("Description of Normalized Data:")
print(np.round(x_train_scaled.describe(), 1))
