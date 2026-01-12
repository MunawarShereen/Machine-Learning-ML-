import pandas as pd
from ydata_profiling import ProfileReport

# 1. Load your dataset
df = pd.read_csv('train.csv')

# 2. Create the Profile Report
# This one line calculates everything (mean, nulls, graphs, etc.)
profile = ProfileReport(df, title="Titanic Data Report")

# 3. Save the report as an HTML file
# You can open this file in Google Chrome or any browser
profile.to_file("output.html")
