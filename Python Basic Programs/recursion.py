# Factorial of a number

'''def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))'''
        

# Fibonacci series (nth number)

'''def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(6))'''


#  Sum of natural numbers

'''def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)
    
print(sum(10))'''


# Reverse a string using recursion

'''def reverse(s):
    if len(s) == 0:
        return ""
    else:
        return reverse(s[1:]) + s[0]
    
print(reverse("sunavya"))'''

# Find the power of a number (x^n)

def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)
    
print(power(2, 3))
    