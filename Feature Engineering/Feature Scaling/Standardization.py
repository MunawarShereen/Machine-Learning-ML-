import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/content/Social_Network_Ads.csv')
df = df.iloc[:,2:]
df.sample(5)


from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(
    df.drop("Purchased", axis=1),
    df['Purchased'],
    test_size=0.3,
    random_state=0
)
  
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

scaler.fit(x_train)

x_train_scaler = scaler.transform(x_train)
x_test_scaler = scaler.transform(x_test)

x_train_scaler = pd.DataFrame(x_train_scaler, columns=x_train.columns)
x_test_scaler = pd.DataFrame(x_test_scaler, columns=x_test.columns)
np.round(x_train_scaler.describe(), 1)


