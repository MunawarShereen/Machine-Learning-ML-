import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split

# 1. Sample Data
data = {
    'fever': [98.0, 102.0, None, 99.0],      # Numerical (has missing value)
    'cough': ['Mild', 'Strong', 'Mild', 'Strong'], # Ordinal
    'gender': ['Male', 'Female', 'Female', 'Male'],# Nominal
    'city': ['Karachi', 'Lahore', 'Karachi', 'Islamabad'], # Nominal
    'age': [20, 35, 40, 25]                  # Extra column (will be passed through)
}
df = pd.DataFrame(data)

# 2. Split Data
X_train, X_test, y_train, y_test = train_test_split(df.drop(columns=['age']), df['age'], test_size=0.2)

# 3. Define Column Transformer
transformer = ColumnTransformer(transformers=[
    ('tnf1', SimpleImputer(), ['fever']),
    ('tnf2', OrdinalEncoder(categories=[['Mild','Strong']]), ['cough']),
    ('tnf3', OneHotEncoder(sparse_output=False, drop='first'), ['gender','city'])
], remainder='passthrough')

# 4. Apply Transformation
# We fit only on training data, and transform both
X_train_transformed = transformer.fit_transform(X_train)
X_test_transformed = transformer.transform(X_test)

# Display Result shape
print("Original Shape:", X_train.shape)
print("Transformed Shape:", X_train_transformed.shape)
