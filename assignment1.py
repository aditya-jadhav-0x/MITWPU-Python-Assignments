# --- 1. LIST OPERATIONS ---
# Creating an initial list of students
student_list = ["Amit", "Rahul", "Sneha"]
print("Original List:", student_list)

# Adding a student to the list
student_list.append("Pooja")
print("List after Add:", student_list)

# Updating a student in the list
student_list[1] = "Rohit"
print("List after Update:", student_list)

# Deleting a student from the list
student_list.remove("Sneha")
print("List after Delete:", student_list)
print("-" * 30)

# --- 2. TUPLE OPERATIONS ---
# Note: Tuples cannot be modified directly, so we convert to a list to change it
student_tuple = ("Yash", "Ananya", "Rohan")
print("Original Tuple:", student_tuple)

# Adding to tuple (convert to list, append, convert back)
temp_list1 = list(student_tuple)
temp_list1.append("Tanvi")
student_tuple = tuple(temp_list1)
print("Tuple after Add:", student_tuple)

# Updating tuple (convert to list, change index, convert back)
temp_list2 = list(student_tuple)
temp_list2[2] = "Raj"
student_tuple = tuple(temp_list2)
print("Tuple after Update:", student_tuple)

# Deleting from tuple (convert to list, remove, convert back)
temp_list3 = list(student_tuple)
temp_list3.remove("Yash")
student_tuple = tuple(temp_list3)
print("Tuple after Delete:", student_tuple)
print("-" * 30)

# --- 3. DICTIONARY OPERATIONS ---
# Creating a dictionary with Roll No as Key and Name as Value
student_dict = {101: "Aditya", 102: "Neha", 103: "Gaurav"}
print("Original Dictionary:", student_dict)

# Adding a new key-value pair
student_dict[104] = "Riya"
print("Dictionary after Add:", student_dict)

# Updating an existing value
student_dict[102] = "Nisha"
print("Dictionary after Update:", student_dict)

# Deleting a key-value pair
del student_dict[103]
print("Dictionary after Delete:", student_dict)

# ==========================================
# ASSIGNMENT 1: CORE DATA STRUCTURES
# ==========================================

# ------------------------------------------
# QUESTION 1: Dictionary Operations
# ------------------------------------------
print("--- QUESTION 1 ---")
my_dict1 = {
    1: "Aman",
    2: "Bhavna",
    3: "Chirag",
    4: "Divya",
    5: "Esha"
}
print("Initial dictionary:", my_dict1)

# Add student information
my_dict1[6] = "Faizan"
print("After adding key 6:", my_dict1)

# Delete student information
del my_dict1[3]
print("After deleting key 3:", my_dict1)
print("\n" + "="*40 + "\n")


# ------------------------------------------
# QUESTION 2: Convert Two Lists to a Dictionary
# ------------------------------------------
print("--- QUESTION 2 ---")
list1 = ['name', 'panel', 'rollno']
list2 = ['ABC', 'B', 34]
my_dict2 = {}

for i in range(len(list1)):
    key = list1[i]
    value = list2[i]
    my_dict2[key] = value

print("Converted Dictionary:", my_dict2)
print("\n" + "="*40 + "\n")


# ------------------------------------------
# QUESTION 3: Sort elements of the dictionary
# ------------------------------------------
print("--- QUESTION 3 ---")
my_dict3 = {
    'name': 'ABC', 
    'panel': 'B', 
    'rollno': 34, 
    'marks': [65, 87, 67, 94]
}
sorted_keys = sorted(my_dict3)
print("Sorted keys list:", sorted_keys)
print("\n" + "="*40 + "\n")


# ------------------------------------------
# QUESTION 4: Convert a dictionary to lists
# ------------------------------------------
print("--- QUESTION 4 ---")
my_dict4 = {'name': 'ABC', 'panel': 'B', 'rollno': 34}
keys_list = []
values_list = []

for k in my_dict4:
    keys_list.append(k)
    values_list.append(my_dict4[k])

print("List of keys:", keys_list)
print("List of values:", values_list)
print("\n" + "="*40 + "\n")


# ------------------------------------------
# QUESTION 5: Find the mean of values
# ------------------------------------------
print("--- QUESTION 5 ---")
mydict5 = {'marks1': 23, 'marks2': 123, 'marks3': 43, 'marks4': 13, 'marks5': 39}
total_sum = 0
count = 0

for k in mydict5:
    total_sum = total_sum + mydict5[k]
    count = count + 1

mean_value = total_sum / count
print("Mean of all values:", mean_value)
print("\n" + "="*40 + "\n")


# ------------------------------------------
# QUESTION 6: Operations on complex dictionary
# ------------------------------------------
print("--- QUESTION 6 ---")
my_dict6 = {
    'name': ['Yash', 'Neel', 'Dev'], 
    'rollno':, 
    'marks': [78, 56, 98]
}

# a) Display name as Dev
print("a) Name as Dev:", my_dict6['name'][2])

# b) Display 12 roll no
print("b) Roll no 12:", my_dict6['rollno'][1])

# c) Display greatest marks
marks_list = my_dict6['marks']
highest = marks_list[0]
for m in marks_list:
    if m > highest:
        highest = m
print("c) Greatest marks:", highest)
print("\n" + "="*40 + "\n")


# ------------------------------------------
# QUESTION 7: Calculate frequency of letters
# ------------------------------------------
print("--- QUESTION 7 ---")
input_string = "hello mit wpu"
frequency_dict = {}

for letter in input_string:
    if letter in frequency_dict:
        frequency_dict[letter] = frequency_dict[letter] + 1
    else:
        frequency_dict[letter] = 1

print("Letter frequencies:", frequency_dict)
print("\n" + "="*40 + "\n")


# ------------------------------------------
# QUESTION 8: Quotient and Remainder Tuple
# ------------------------------------------
print("--- QUESTION 8 ---")
num = int(input("Enter numerator: "))
den = int(input("Enter denominator: "))

quotient = num // den
remainder = num % den
output_tuple = (quotient, remainder)

print("Result tuple (Quotient, Remainder):", output_tuple)
print("\n" + "="*40 + "\n")


# ------------------------------------------
# QUESTION 9: Days between two date tuples
# ------------------------------------------
print("--- QUESTION 9 ---")
import datetime

print("Enter First Date:")
d1 = int(input("Day 1: "))
m1 = int(input("Month 1: "))
y1 = int(input("Year 1: "))
date1_tuple = (d1, m1, y1)

print("Enter Second Date:")
d2 = int(input("Day 2: "))
m2 = int(input("Month 2: "))
y2 = int(input("Year 2: "))
date2_tuple = (d2, m2, y2)

py_date1 = datetime.date(date1_tuple[2], date1_tuple[1], date1_tuple[0])
py_date2 = datetime.date(date2_tuple[2], date2_tuple[1], date2_tuple[0])

difference = py_date2 - py_date1
days_between = abs(difference.days)

print("Number of days between dates:", days_between)
print("\n" + "="*40 + "\n")
