# Q6:- Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.


# For example:
# Input: heads -> 4, legs -> 12
# Output: dogs -> 2 chicken -> 2

# Problem Understanding:
# Each dog has 1 head and 4 legs.
# Each chicken has 1 head and 2 legs.

# Given total heads and total legs, find how many dogs and chickens there are.
# Formula:
# Let:𝑑 = number of dogs
# Let:c = number of chickens


# For heads:
# d + c = total_heads

# For legs:
# 4d + 2c = total_legs

# Input from user
total_legs = int(input("Enter total number of legs: "))
total_heads = int(input("Enter total number of heads: "))

# Calculate number of dogs and chickens
total_dog = (total_legs - (2 * total_heads)) // 2
total_chicken = total_heads - total_dog

# Check for validity
if total_dog < 0 or total_chicken < 0 or (4*total_dog + 2*total_chicken != total_legs):
    print("Invalid input. Please check the numbers of heads and legs.")
else:
    print(f"Total Dogs -> {total_dog}")
    print(f"Total Chicken -> {total_chicken}")


