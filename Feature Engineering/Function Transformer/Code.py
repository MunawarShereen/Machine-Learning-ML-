import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
from sklearn.preprocessing import FunctionTransformer

# Function to draw Histogram and QQ Plot side-by-side
def plot_data(df, feature):
    plt.figure(figsize=(14, 4))
    
    # 1. Histogram (Distplot)
    plt.subplot(1, 2, 1)
    plt.hist(df[feature], bins=30, color='skyblue', edgecolor='black')
    plt.title(f'{feature} Histogram')
    
    # 2. QQ Plot
    plt.subplot(1, 2, 2)
    stats.probplot(df[feature], dist="norm", plot=plt)
    plt.title(f'{feature} QQ Plot')
    
    plt.show()

# ==========================================
# 1. Create Dummy Data (Right Skewed)
# ==========================================
# Exponential distribution is naturally right-skewed
data = {'Age': np.random.exponential(scale=2, size=1000)}
df = pd.DataFrame(data)

print("Original Right Skewed Data:")
plot_data(df, 'Age')

# ==========================================
# 2. Log Transformer (For Right Skew)
# ==========================================
# func=np.log1p is safe (log(1+x)) to avoid error on 0
log_transformer = FunctionTransformer(func=np.log1p)

df['Age_Log'] = log_transformer.transform(df[['Age']])

print("\nAfter Log Transform (Normal-like):")
plot_data(df, 'Age_Log')

# ==========================================
# 3. Square Transformer (For Left Skew)
# ==========================================
# Creating dummy Left Skewed data
df['Left_Skewed'] = 20 - np.random.exponential(scale=2, size=1000)

print("\nOriginal Left Skewed Data:")
plot_data(df, 'Left_Skewed')

square_transformer = FunctionTransformer(func=np.square)
df['Left_Skewed_Squared'] = square_transformer.transform(df[['Left_Skewed']])

print("\nAfter Square Transform:")
plot_data(df, 'Left_Skewed_Squared')

# ==========================================
# 4. Reciprocal Transformer (1/x)
# ==========================================
reciprocal_transformer = FunctionTransformer(func=np.reciprocal)

# Note: Adding +1 to avoid division by zero error if any 0 exists
df['Age_Reciprocal'] = reciprocal_transformer.transform(df[['Age']] + 1)

print("\nAfter Reciprocal Transform:")
plot_data(df, 'Age_Reciprocal')
