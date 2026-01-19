import pandas as pd
import numpy as np

# ==========================================
# 1. Create Dummy Data
# ==========================================
data = {
    # Scenario A: Mixed values in different rows (Some numbers, some text)
    'ticket_mixed': ['12345', 'A543', '67890', 'W.E.P', '2468', 'S.O.C'],
    
    # Scenario B: Mixed values in ONE cell (Letter + Number)
    'cabin_mixed': ['C85', 'C123', 'E46', 'G6', 'C2', 'D33']
}
df = pd.DataFrame(data)

print("Original Data:")
print(df)
print("-" * 30)

# ==========================================
# 2. Handling Scenario A (Mixed Rows)
# ==========================================
# Step 1: Extract Numerical part
# 'errors=coerce' converts 'A543' and 'W.E.P' into NaN
df['ticket_num'] = pd.to_numeric(df["ticket_mixed"], errors='coerce', downcast='integer')

# Step 2: Extract Categorical part
# If ticket_num is null (meaning it was text), take original value. Else put NaN.
df['ticket_cat'] = np.where(df['ticket_num'].isnull(), df['ticket_mixed'], np.nan)

print("Scenario A Result (Split Rows):")
print(df[['ticket_mixed', 'ticket_num', 'ticket_cat']])
print("-" * 30)

# ==========================================
# 3. Handling Scenario B (Mixed Cells)
# ==========================================
# Step 1: Extract Categorical part (First letter)
df['cabin_cat'] = df['cabin_mixed'].str[0] 

# Step 2: Extract Numerical part (Using Regex to find digits)
# (\d+) means "find a group of digits"
df['cabin_num'] = df['cabin_mixed'].str.extract('(\d+)')

print("Scenario B Result (Split Cell):")
print(df[['cabin_mixed', 'cabin_cat', 'cabin_num']])
