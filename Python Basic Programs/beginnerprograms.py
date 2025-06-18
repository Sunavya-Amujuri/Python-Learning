## Write a program to check, wheather the number is even or odd.

'''num = int(input("Give a number: "))

if num % 2 == 0:
    print("Given number is true.")
else:
    print("Given number is false.")'''


## Write a Python program to calculate the factorial of a given positive integer.


'''n = int(input("Give a number: "))

if n < 0:
        print("Factorial does not exists for negative numbers.")
elif n == 0:
        print ("Factorial of 0 is 1.")
else:
    factorial = 1
    for i in range (1,n+1):
        factorial *= i
    print("Factorial of", n ,"is: ",factorial)'''


## Reversing a number.
        
'''n = int(input("Enter a number: "))
reversed_num = 0

while n > 0:
    digit = n % 10
    reversed_num = reversed_num * 10 + digit
    n = n // 10
    
print("Reversed_number: ", reversed_num)
'''

## Calculator Program – Using functions (+, −, ×, ÷, %, etc.)

'''a = int(input("Give a value: "))
b = int(input("Give b value: "))

print(f"Addition: {a+b}")
print(f"Subtraction: {a-b}")
print(f"Multiplication: {a*b}")
print(f"Division: {a/b}")
print(f"Modulus: {a%b}")'''

    
## Largest of Three Numbers

'''num1 = int(input("Give a value: "))
num2 = int(input("Give b value: "))
num3 = int(input("Give c value: "))

if num1 >= num2 and num1 >= num3:
    print ("Greatest number is: ", num1)
elif num2 >= num1 and num2 >= num3:
    print ("Greatest number is: ", num2)
else:
    print ("Greatest number is: ", num3)'''


## Check prime number.

'''num = int(input("Give a number: "))

if num <= 1:
    print("Given number is not prime.")
else:
    is_prime = True
    for i in range(2,int(num*0.5)+1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print("Given number is prime.")
else:
    print("Given is not not prime.")'''


## Program for simple and compound interest

'''p = float(input("Give Principle amount value: "))
r = float(input("Give rate value: "))
t = float(input("Give time value: "))

SI = 0
CI = 0
d = (1+(r/100))**t

SI = p*r*t/100
CI = p*d-p

print("Simple Interest: ", SI)
print("Compound Interest: ", CI)'''

## Multiplication table generator

num = int(input("Give a number: "))

for i in range(1,11):
    print(f"{num} x {i} = {num*i}")
   


 

