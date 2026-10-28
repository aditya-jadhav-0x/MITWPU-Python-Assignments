import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Loading the dataset
# Replace 'student_marks.csv' with the actual path of your file
try:
    df = pd.read_csv("student_marks.csv")
    print("Dataset loaded successfully.\n")
except FileNotFoundError:
    # Programmatic creation of the exact dataset specified in the assignment manual
    print("CSV file not found. Creating the sample dataset automatically...")
    data = {
        "Student": ["Amit", "Bhavna", "Chetan", "Diya", "Esha", "Farhan"],
        "Maths":,
        "Python":,
        "Attendance":,
        "City": ["Pune", "Mumbai", "Pune", "Nashik", "Mumbai", "Pune"]
    }
    df = pd.DataFrame(data)

# 2. Display the dataset
print("\n--- Student Dataset ---")
print(df)

# 3. Line Plot (Python Marks per Student)
plt.figure(figsize=(6, 4))
plt.plot(df["Student"], df["Python"], marker='o', color='blue', linestyle='-', linewidth=2)
plt.title("Line Plot: Student vs Python Marks")
plt.xlabel("Student Name")
plt.ylabel("Python Marks")
plt.grid(True)
plt.show()

# 4. Bar Plot (Maths Marks per Student)
plt.figure(figsize=(6, 4))
plt.bar(df["Student"], df["Maths"], color='green', edgecolor='black')
plt.title("Bar Plot: Student vs Maths Marks")
plt.xlabel("Student Name")
plt.ylabel("Maths Marks")
plt.grid(axis='y')
plt.show()

# 5. Scatter Plot (Maths vs Python Marks)
plt.figure(figsize=(6, 4))
plt.scatter(df["Maths"], df["Python"], color='red', s=100, edgecolor='black')
plt.title("Scatter Plot: Maths vs Python Marks")
plt.xlabel("Maths Marks")
plt.ylabel("Python Marks")
plt.grid(True)
plt.show()

# 6. Correlation Matrix Analysis
print("\n--- Correlation Matrix ---")
# Dropping non-numerical columns ('Student' and 'City') before correlation calculation
numerical_df = df.drop(columns=["Student", "City"])
corr_matrix = numerical_df.corr()
print(corr_matrix)

# 7. Heatmap Generation
plt.figure(figsize=(6, 4))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=0.5, fmt=".2f")
plt.title("Heatmap: Attribute Correlation Matrix")
plt.show()
