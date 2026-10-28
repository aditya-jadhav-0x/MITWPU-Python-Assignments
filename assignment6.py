import pandas as pd

# 1. Loading the dataset
# Replace 'dataset.csv' with the actual path of your file
try:
    df = pd.read_csv("dataset.csv")
    print("Dataset loaded successfully.\n")
except FileNotFoundError:
    # Creating a fallback sample dataset if the file does not exist
    print("File not found. Creating a sample DataFrame for demonstration...")
    data = {
        "Roll_No":,
        "Name": ["Amit", "Rahul", "Sneha", "Amit", "Priya", "Vikram"],
        "Marks": [85.0, None, 92.0, 85.0, 78.0, None],
        "City": ["Pune", "Mumbai", "Pune", "Pune", "Delhi", "Mumbai"],
    }
    df = pd.DataFrame(data)

# 2. Basic Data Exploration
print("--- Initial Dataset ---")
print(df.head())  # Displays the first 5 rows

print("\n--- Structural Information ---")
df.info()  # Displays column data types and non-null counts

print("\n--- Statistical Summary ---")
print(df.describe(include="all"))

# 3. Handling Duplicate Records
print("\n--- Checking for Duplicates ---")
print("Duplicate rows mask:\n", df.duplicated())

# Removing duplicate records permanently
df = df.drop_duplicates()
print("\nDataset after removing duplicates:")
print(df)

# 4. Handling Missing Values
print("\n--- Checking for Missing Values ---")
print(df.isnull().sum())

# Strategy: Filling missing numerical data in 'Marks' with the mean value
mean_marks = df["Marks"].mean()
df["Marks"] = df["Marks"].fillna(mean_marks)
print(f"\nMissing values handled (Filled with Mean Marks = {mean_marks}):")
print(df)

# 5. Data Selection and Filtering using loc[]
print("\n--- Filtering Data using loc[] ---")
# Selecting records where City is 'Pune'
pune_students = df.loc[df["City"] == "Pune"]
print("Students located in Pune:")
print(pune_students)
