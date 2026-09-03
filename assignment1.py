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
