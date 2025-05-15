# Q3: Swap Two Numbers Without Using Special Python Syntax
# Requirement:

# Take 2 numbers as input.
# Swap them with using Python's special syntax like a, b = b, a or tuple unpacking.

# Input from user
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

print(f"\nBefore swapping: a = {a}, b = {b}")

a, b = b, a

print(f"After swapping: a = {a}, b = {b}")
