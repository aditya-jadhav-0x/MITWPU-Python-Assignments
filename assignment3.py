# =====================================================================
# ASSIGNMENT 3: RIGHT-ANGLED TRIANGLE CHECKER USING FUNCTION
# =====================================================================

# Defining the user-defined function
def check_right_triangle(side1, side2, side3):
    # Calculate the square of each side using basic multiplication
    sq1 = side1 * side1
    sq2 = side2 * side2
    sq3 = side3 * side3
    
    # Check Pythagoras theorem for all possible hypotenuse combinations
    if (sq1 + sq2 == sq3) or (sq1 + sq3 == sq2) or (sq2 + sq3 == sq1):
        return True
    else:
        return False

# --- Main Program Flow ---
print("--- ASSIGNMENT 3: TRIANGLE CHECKER ---")

# Accept three side values from the user
s1 = int(input("Enter length of side 1: "))
s2 = int(input("Enter length of side 2: "))
s3 = int(input("Enter length of side 3: "))

# Function Calling: Pass the inputs to our custom function
result = check_right_triangle(s1, s2, s3)

# Display the final output based on the returned True/False value
if result == True:
    print("Output: The triangle IS a right-angled triangle.")
else:
    print("Output: The triangle IS NOT a right-angled triangle.")
