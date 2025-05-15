# Q3: Swap Two Numbers Without Using Special Python Syntax
# Requirement:

# Take 2 numbers as input.
# Swap them without using Python's special syntax like a, b = b, a or tuple unpacking using standard method.

# Input from user
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

print(f"\nBefore swapping: a = {a}, b = {b}")

# Swapping using a temporary variable
temp = a
a = b
b = temp

print(f"After swapping: a = {a}, b = {b}")
