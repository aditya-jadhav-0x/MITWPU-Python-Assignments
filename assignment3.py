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


# =====================================================================
# ASSIGNMENT 3: EXERCISES ON FUNCTION
# =====================================================================

# ---------------------------------------------------------------------
# EXERCISE 1: Display Prime Factors of a Number
# ---------------------------------------------------------------------
print("\n" + "="*40)
print("--- EXERCISE 1: PRIME FACTORS ---")
print("====================================")

def find_prime_factors(n):
    factors_list = []
    divisor = 2
    temp = n
    
    # Keep dividing by the smallest possible numbers
    while temp > 1:
        if temp % divisor == 0:
            # Check if we already added this factor to prevent duplicates
            if divisor not in factors_list:
                factors_list.append(divisor)
            temp = temp // divisor
        else:
            divisor = divisor + 1
            
    print("Prime factors are:", factors_list)

# Take input from user
input_no = int(input("Enter number to find prime factors: "))
find_prime_factors(input_no)


# ---------------------------------------------------------------------
# EXERCISE 2: Print Even Numbers in a Range 1 to 100
# ---------------------------------------------------------------------
print("\n" + "="*40)
print("--- EXERCISE 2: EVEN NUMBERS 1 TO 100 ---")
print("====================================")

def print_even_numbers():
    # Loop from 1 to 100
    for num in range(1, 101):
        if num % 2 == 0:
            print(num)

# Call the function to print out numbers
print_even_numbers()


# ---------------------------------------------------------------------
# EXERCISE 3: Quadratic Equation with Exception Handling
# ---------------------------------------------------------------------
print("\n" + "="*40)
print("--- EXERCISE 3: QUADRATIC EQUATION ROOTS ---")
print("====================================")

import math

def calculate_quadratic_roots():
    try:
        # Accept three coefficients from the user
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))
        
        # Formula for discriminant: b^2 - 4ac
        discriminant = (b * b) - (4 * a * c)
        
        # The math.sqrt will automatically throw a ValueError if discriminant < 0
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        
        print("Root 1:", root1)
        print("Root 2:", root2)
        
    except ValueError:
        print("Error caught: math domain error (Discriminant is negative, roots are imaginary)")
    except NameError:
        print("Error caught: NameError (A variable name is misspelled or missing)")
    except TypeError:
        print("Error caught: TypeError (Wrong data type used in math calculation)")

# Call the function to execute logic boundaries
calculate_quadratic_roots()
print("="*40 + "\n")

