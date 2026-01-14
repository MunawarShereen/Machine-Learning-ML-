import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from sklearn.preprocessing import PowerTransformer

# Helper function to check if data is Normal (Histogram + QQ Plot)
def plot_data(df, feature, title):
    plt.figure(figsize=(14, 4))
    
    # 1. Histogram (To see shape)
    plt.subplot(1, 2, 1)
    sns.histplot(df[feature], kde=True, color='purple')
    plt.title(f'{title} - Histogram')
    
    # 2. QQ Plot (To check Normality - Dots should be on the red line)
    plt.subplot(1, 2, 2)
    stats.probplot(df[feature], dist="norm", plot=plt)
    plt.title(f'{title} - QQ Plot')
    
    plt.show()

# ==========================================
# 1. Create Dummy Data
# ==========================================
np.random.seed(42)
# Create right-skewed data (Log-Normal)
data = {'Score': np.random.lognormal(mean=0, sigma=1, size=1000)}
df = pd.DataFrame(data)

# Create a column with Negative values for Yeo-Johnson
df['Score_Negative'] = df['Score'] - df['Score'].mean()

print("Original Data:")
plot_data(df, 'Score', 'Original Positive Data')

# ==========================================
# 2. Box-Cox Transformation
# ==========================================
# Note: Can ONLY be used on strictly positive data (>0)
pt_boxcox = PowerTransformer(method='box-cox')

# fit_transform calculates the best Lambda and applies it
df['Score_BoxCox'] = pt_boxcox.fit_transform(df[['Score']])

print("\nAfter Box-Cox Transformation:")
plot_data(df, 'Score_BoxCox', 'Box-Cox Result')

# ==========================================
# 3. Yeo-Johnson Transformation
# ==========================================
# Note: Can be used on Negative data too
pt_yeo = PowerTransformer(method='yeo-johnson')

df['Score_YeoJohnson'] = pt_yeo.fit_transform(df[['Score_Negative']])

print("\nAfter Yeo-Johnson Transformation:")
plot_data(df, 'Score_YeoJohnson', 'Yeo-Johnson Result')
