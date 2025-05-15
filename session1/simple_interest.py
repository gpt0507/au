# Q5:- Write a program to find the simple interest when the value of principle,rate of interest and time period is provided by the user.


# Formula: Simple Interest (SI)= (Principal×Rate×Time)/100

# Principal = initial amount

# Rate = rate of interest per annum (in %)

# Time = time period (in years)


# Take input from user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time period (in years): "))

# Calculate simple interest
simple_interest = (principal * rate * time) / 100

# Display the result
print(f"Simple Interest is: {simple_interest}")
