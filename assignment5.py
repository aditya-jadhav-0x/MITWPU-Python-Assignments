import re

# 1. Variable Declaration & User Input
user_string = input("Enter a string: ")

# 2. Regular Expression Pattern Definition (a-z, A-Z, 0-9)
pattern = "^[a-zA-Z0-9]+$"

# 3. Pattern Matching Logic (Conditional Check)
if re.match(pattern, user_string):
    # 4. User Output (Success case)
    print("The string contains only allowed characters.")
else:
    # 4. User Output (Failure case)
    print("The string contains invalid characters or spaces.")
