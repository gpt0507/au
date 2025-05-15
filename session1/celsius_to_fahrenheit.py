# Q2:- Write a program that will convert celsius value to fahrenheit.
# Formula: Fahrenheit=(Celsius×9/5)+32

# Celsius to Fahrenheit converter

# Input from user
celsius = float(input("Enter temperature in Celsius: "))

# Conversion formula
fahrenheit = (celsius * 9/5) + 32

# Output result
print(f"{celsius}°C is equal to {fahrenheit}°F")
print(str(celsius), "°C is equal to", str(fahrenheit), "°F")
