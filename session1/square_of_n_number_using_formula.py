# Input from user
n = int(input("Enter a positive integer n: "))

# Calculate sum of squares using formula
sum_squares = n * (n + 1) * (2*n + 1) // 6

print(f"Sum of squares of first {n} natural numbers is: {sum_squares}")
