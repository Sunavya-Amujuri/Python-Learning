'''Create a basic calculator program that performs add, sub, mul, division.
Ask the user to enter 2 numbers & choose an operator. Display the result accordingly.'''

num1 = int(input("Give 1st number: "))
num2 = int(input("Give 2nd number: "))
operator = input("Give operator: ")

if operator == "+":
    print(f"Addition of 2 numbers is {num1+num2}")
elif operator == "-":
    print(f"Sutraction of 2 numbers is {num1-num2}")
elif operator == "*":
    print(f"Multiplication of 2 numbers is {num1*num2}")
elif operator == "/":
    print(f"Division of 2 numbers is {num1/num2}")
else:
    print("Invalid Operator")

