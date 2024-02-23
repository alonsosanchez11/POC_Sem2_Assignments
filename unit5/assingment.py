number1 = 0
number2 = 0
try:
    number1 = int(input("Enter a number"))
    number2 = int(input("Enter a number"))

except ValueError:
    print("integer was not given")
    

try:
   answer = number1 / number2
   print("The answer is", answer)  
except ZeroDivisionError:
    print("division by zero is not possible")