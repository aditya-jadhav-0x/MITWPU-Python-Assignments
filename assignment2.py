# Taking three integer inputs from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

# Comparing numbers using basic if-elif-else logic
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3

# Printing the final output
print("The largest number is:", largest)

#-----------------------------
# Accept Marks in Math from user
math_marks = int(input("Enter your Mathematics marks: "))

# Multi-condition chain to find the grade
if math_marks >= 90 and math_marks <= 100:
    grade = "O"
elif math_marks >= 80 and math_marks <= 89:
    grade = "A+"
elif math_marks >= 70 and math_marks <= 79:
    grade = "A"
elif math_marks >= 60 and math_marks <= 69:
    grade = "B"
elif math_marks >= 50 and math_marks <= 59:
    grade = "C"
elif math_marks >= 40 and math_marks <= 49:
    grade = "P"
else:
    grade = "F"

# Display calculated grade output
print("Your assigned Grade is:")
print(grade)
