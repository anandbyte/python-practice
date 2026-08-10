# Find Largest number between two number

num1 = float(input("Enter your first number"))
num2 = float(input("Enter your Second number"))
if num1 < num2:
  print("Largest Number is",num2)
elif num1 > num2:
  print("Largest num is",num1)
else:
  print("Both numbers are equal")
