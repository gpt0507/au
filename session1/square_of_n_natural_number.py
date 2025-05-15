# Q7:- Write a program to find the sum of squares of first n natural numbers where n will be provided by the user.

# Input from user
n = int(input("Enter a positive integer n: "))

# Initialize sum
sum_squares = 0

# Calculate sum of squares using loop
for i in range(1, n+1):
    sum_squares += i**2

print(f"Sum of squares of first {n} natural numbers is: {sum_squares}")
