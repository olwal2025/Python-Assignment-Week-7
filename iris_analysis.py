# Importing the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Step 1: Load the Iris dataset from sklearn with error handling
try:
    iris_data = load_iris()
except Exception as e:
    print("Error loading the Iris dataset:", e)
    exit(1)

# Step 2: Create a DataFrame from the data
iris_df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)

# Step 3: Add a species column using the target values
iris_df['species'] = iris_data.target
iris_df['species'] = iris_df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

# Step 4: View the first few rows of the dataset
print(" Preview of the dataset:")
print(iris_df.head())

# Step 5: Check the structure of the dataset
print("\n Dataset Info:")
print(iris_df.info())

# Step 6: Check for any missing data
print("\n Any missing values?")
print(iris_df.isnull().sum())

# Step 7: Basic statistical summary
print("\n Summary Statistics:")
print(iris_df.describe())

# Step 8: Group by species to see average values
print("\n Average measurements by species:")
grouped_data = iris_df.groupby('species').mean()
print(grouped_data)

# ---- Data Visualizations ----

# Line Plot - Sepal Length (just to try a line chart)
iris_sorted = iris_df.sort_values(by='sepal length (cm)')
plt.figure(figsize=(8, 5))
plt.plot(iris_sorted['sepal length (cm)'].values, color='green')
plt.title("Sepal Length Line Plot (sorted)")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.grid(True)
plt.tight_layout()
plt.show()

# Bar Chart - Average petal length per species
plt.figure(figsize=(8, 5))
grouped_data['petal length (cm)'].plot(kind='bar', color=['#a2d5c6', '#077b8a', '#5c3c92'])
plt.title("Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.tight_layout()
plt.show()

# Histogram - Distribution of Sepal Width
plt.figure(figsize=(8, 5))
plt.hist(iris_df['sepal width (cm)'], bins=12, color='orange', edgecolor='black')
plt.title("Histogram of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Scatter Plot - Sepal Length vs Petal Length
plt.figure(figsize=(8, 6))
sns.scatterplot(data=iris_df, x='sepal length (cm)', y='petal length (cm)', hue='species', palette='Set2')
plt.title("Scatter Plot: Sepal vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.tight_layout()
plt.show()

# Final Observations
print("\n Observations:")
print("- Virginica flowers tend to have longer petals.")
print("- There is a positive relationship between sepal length and petal length.")
print("- Setosa species have smaller petal lengths but wider sepals compared to others.")
