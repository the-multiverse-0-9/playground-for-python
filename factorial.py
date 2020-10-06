# Program to find the factorial of a number
num = int(input("Enter a number: "))                        # Takes the number as input               
factorial = 1
if num < 0:
   print("Factorial does not exist for negative numbers.")  # Prints output
elif num == 0:
   print("The factorial of 0 is 1")                         # Prints output
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of", num, "is", factorial)          # Prints output
