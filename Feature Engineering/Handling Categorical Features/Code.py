# ===============================
# ORDINAL ENCODING
# ===============================
from sklearn.preprocessing import OrdinalEncoder
import pandas as pd

# Sample data
df_ordinal = pd.DataFrame({
    'Education': ['School', 'College', 'University', 'College']
})

# Ordinal Encoding (order matters)
ordinal_enc = OrdinalEncoder(categories=[['School', 'College', 'University']])
df_ordinal['Education_Encoded'] = ordinal_enc.fit_transform(df_ordinal[['Education']])

print("Ordinal Encoding:")
print(df_ordinal)


# ===============================
# LABEL ENCODING (TARGET ONLY)
# ===============================
from sklearn.preprocessing import LabelEncoder

# Sample target variable
y = pd.Series(['Yes', 'No', 'Yes', 'No'])

label_enc = LabelEncoder()
y_encoded = label_enc.fit_transform(y)

print("\nLabel Encoding (Target Variable):")
print(y_encoded)


# ===============================
# ONE HOT ENCODING (NOMINAL DATA)
# ===============================
from sklearn.preprocessing import OneHotEncoder

# Sample data
df_nominal = pd.DataFrame({
    'Color': ['Red', 'Green', 'Blue', 'Red']
})

# One Hot Encoding with n-1 rule
ohe = OneHotEncoder(drop='first', sparse=False)
encoded_array = ohe.fit_transform(df_nominal[['Color']])

# Convert to DataFrame
df_ohe = pd.DataFrame(
    encoded_array,
    columns=ohe.get_feature_names_out(['Color'])
)

print("\nOne Hot Encoding (Nominal Data):")
print(df_ohe)
