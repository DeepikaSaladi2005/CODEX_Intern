import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV File
csv_file = "Iris.csv"  # Replace with your CSV file path
df = pd.read_csv(csv_file)

# Display first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Basic Data Summary
print("\nDataset Summary:")
print(df.describe())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Select a numeric column (modify this based on your dataset)
column_name = "Sales"  # Replace with your column name
if column_name in df.columns:
    avg_value = df[column_name].mean()
    print(f"\nAverage {column_name}: {avg_value:.2f}")

    # Bar Chart
    plt.figure(figsize=(10, 5))
    df[column_name].plot(kind="bar", color="skyblue", alpha=0.7)
    plt.title(f"Bar Chart of {column_name}")
    plt.xlabel("Index")
    plt.ylabel(column_name)
    plt.show()

# Scatter Plot (Modify columns as needed)
x_column = "Marketing Spend"  # Replace with actual column name
y_column = "Sales"  # Replace with actual column name
if x_column in df.columns and y_column in df.columns:
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x=df[x_column], y=df[y_column], color="red")
    plt.title(f"Scatter Plot: {x_column} vs {y_column}")
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.show()
# Exclude non-numeric columns before calculating correlation
numeric_df = df.select_dtypes(include=['number'])  # Select only numeric columns
plt.figure(figsize=(8, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Heatmap of Correlation Matrix")
plt.show()

# Heatmap for Correlation Matrix
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Heatmap of Correlation Matrix")
plt.show()
