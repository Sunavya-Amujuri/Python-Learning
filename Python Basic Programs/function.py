''' 1) Finding sum of two numbers using function.'''

'''a = int(input())
b = int(input())

def add2numbers(a,b):       #add2numbers(c,d)
    print(a+b)              #print(c+d)
add2numbers(a,b)            #add2numbers(a,b)
'''

''' 2) Finding area of circle using function.'''

'''def area(r = 1):
    circleArea = 3.14*(r**2)
    return circleArea
radius = 2
a = area(radius)

print(a)'''


''' 3) solving Quadratic Equations.'''

'''a = int(input("Give a : "))
b = int(input("Give b : "))
c = int(input("Give c : "))

def calculateroots(a,b,c):
    root1 = 0
    root2 = 0
    d = (b**2)- 4*a*c
    root1 = (-b + (d**(0.5)))/2*a
    root2 = (-b - (d**(0.5)))/2*a
    print(f"Roots:({root1},{root2})")

calculateroots(a,b,c)'''


''' 4) Swaping of two numbers.'''

'''a = int(input("Give a: "))
b = int(input("Give b: "))

def swap(a,b):
    b = b+a
    a = b-a
    b = b-a
    print(f"Value of a: {a}")       
    print(f"Value of b: {b}") 

swap(a,b)'''

#or 

a = int(input("Give a: "))
b = int(input("Give b: "))

def swap(a=5,b=10):
    b = b+a
    a = b-a
    b = b-a
    print(f"Value of a: {a}")       
    print(f"Value of b: {b}") 

swap(5,10)
swap(20,30)
swap(5,9)

