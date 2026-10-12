# 1.9 Performance Assessment
# Data Types and Basic Math Operators

name = input("Enter your name: ")
student_id = input("Enter your Student ID: ")

number1 = int(input("Enter your first whole number: "))
number2 = int(input("Enter your second whole number: "))

# Perform three calculations
addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2

# Display calculation results with two decimal places
print("\nCalculation Results:")
print(f"{number1} + {number2} = {addition:.2f}")
print(f"{number1} - {number2} = {subtraction:.2f}")
print(f"{number1} * {number2} = {multiplication:.2f}")

# Compare the two numbers
if number1 > number2:
    print(f"\n{number1} is larger than {number2}.")
elif number1 < number2:
    print(f"\n{number1} is smaller than {number2}.")
else:
    print("\nThe numbers are equal.")

# Display student information
print(f"\nName: {name}")
print(f"Student ID: {student_id}")
