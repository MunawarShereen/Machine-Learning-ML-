import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the datasets
df_train = pd.read_csv('train.csv')       # Titanic Data
df_placement = pd.read_csv('placement.csv') # Placement Data


#Univariate Analysis Code


# A. Histogram (Numerical Column)
# Set the figure size (width, height)
plt.figure(figsize=(8, 5))
# Plot Histogram for Age column
sns.histplot(df_train['Age'], kde=True, color='skyblue')
plt.show()


#B. Countplot (Categorical Column)
plt.figure(figsize=(6, 5))
# Count how many people Survived (0 or 1)
sns.countplot(x='Survived', data=df_train, palette='pastel')
plt.title('Univariate: Count of Survived')
plt.show()



#2. Multivariate Analysis Code


#A. Scatterplot (Numerical - Numerical)
plt.figure(figsize=(8, 6))
# Plot Scatterplot
# x-axis: cgpa, y-axis: iq
# hue: colors points based on 'placement' column
sns.scatterplot(x='cgpa', y='iq', hue='placement', data=df_placement)
plt.title('Multivariate: CGPA vs IQ')
plt.show()

#B. BarPlot (Numerical - Categorical)
plt.figure(figsize=(8, 6))

# Plot Barplot
# x-axis: Pclass (Categorical), y-axis: Fare (Numerical)
# hue: splits bars by Gender
sns.barplot(x='Pclass', y='Fare', hue='Sex', data=df_train)
plt.title('Multivariate: Average Fare by Pclass and Sex')
plt.show()

#C. Distplot / KDE Plot (Numerical - Categorical)
plt.figure(figsize=(8, 6))

# KDE Plot (Kernel Density Estimate) is like a smooth histogram
# fill=True fills the area with color
sns.kdeplot(x='Age', hue='Survived', data=df_train, fill=True)
plt.title('Multivariate: Age Distribution by Survival Status')
plt.show()

#D. ClusterMap (Categorical - Categorical)
# Step 1: Create a Crosstab (Matrix)
# This counts how many people are in each combination of Pclass and Survived
pd_crosstab = pd.crosstab(df_train['Pclass'], df_train['Survived'])

# Step 2: Plot ClusterMap
# annot=True writes the numbers inside the boxes
# cmap="Blues" sets the color theme to blue
sns.clustermap(pd_crosstab, cmap="Blues", annot=True, fmt='d')
plt.title('ClusterMap: Pclass vs Survived')
plt.show()
