### Note: if empty space or num or chr increases use (i+1)  and same way decreases use (i, n)/(n-i).

# 1. Increasing triangle pattern.

'''n = 5
for i in range(n):
    for j in range(i+1):
        print("*", end = " ")
    print()'''

# 2. Decreasing triangle pattern.

'''n = 5
for i in range(n):
    for j in range(i, n):
        print("*", end=" ")
    print()'''

# 3. Right sided triangle.

'''n = 5
for i in range(n):
    for j in range(i, n):
        print(" ", end = "")
    for j in range(i+1):
        print("*", end = "")
    print()'''

# 4. Inverted right sided triangle.

'''n = 5
for i in range(n):
    for j in range(i+1):
        print(" ", end = "")
    for j in range(i, n):
        print("*", end="")
    print()'''

# 5. Hill pattern.

'''n = 5
for i in range(n):
    for j in range(i, n):
        print(" ", end="")
    for j in range(i):
        print("*", end = "")
    for j in range(i+1):
        print("*", end="")
    print()'''

'''n = 5

for i in range(1, n + 1):
    # Print spaces
    print(" " * (n - i), end="")
    
    # Print stars with space
    print("* " * i)'''

# 6. Reverse Hill pattern.

'''n = 5
for i in range(n):
    for j in range(i+1):
        print(" ", end="")
    for j in range(i, n-1):
        print("*", end="")
    for j in range(i, n):
        print("*", end="")
    print()'''

'''n = 5  # height of the diamond (half)

# Upper triangle
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

# Lower triangle
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)'''

'''n = 5
num = 1
for i in range(1, n+1):
    for j in range(i+1):
        print(num, end=" ")
        
    print()'''

'''n = 5 
for i in range(n):
    print(" " * (n-i), end="")
    print(("#" if (i%2==0) else "$") * (i+1))'''

'''n = 5                                                                                                                                                                                   
for i in range(n):
    for j in range(i+1):
        print(" ", end = "")
    for j in range(i, n-1):
        if (i%2==0):
            print("#", end = "")
        else:
            print("$", end = "")
    for j in range(i, n):
        if (i%2==0):
            print("#", end = "")
        else:
            print("$", end = "")

    print()'''

'''n = 5                                                                                                                                                                                   
for i in range(n):
    for j in range(i, n):
        print(" ", end = "")
    for j in range(i):
        if (i%2==0):
            print("#", end = "")
        else:
            print("$", end = "")
    for j in range(i+1):
        if (i%2==0):
            print("#", end = "")
        else:
            print("$", end = "")

    print()'''


'''n = 5
for i in range(n):
    print(" " * (i+1), end="")
    print(("#" if i%2==0 else "$") * (n-i-1), end="")
    print(("#" if i%2==0 else "$") * (n-i))'''

'''n = 5
for i in range(n):
    symbols = ("#" if i%2==0 else "$") * (2 *(n-i)-1)
    spaces = " " * (i+1)
    print(spaces + symbols)'''

'''n = 5
for i in range(n):
    print(" " * (i+1), end="")
    print(("1" if i%2==0 else "0") * (2*(n-i)-1))'''

'''n = 5
for i in range(n):
    symbols = (("1" if i%2==0 else "0") * (2*(n-i)-1))
    spaces = " " * (i+1)
    print(spaces + symbols)'''

#  Diamond pattern

'''n = 5
# Upper half
for i in range(n):
    print(" " * (n - i - 1), end="")
    print("*" * (2 * i + 1))

for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1), end="")
    print("*" * (2 * i + 1))'''

n = 5

'''for i in range(n):
    print(" " * (n-i-1), end="")
    for j in range(i+1):
        print(chr(65+j), end=" ")
        
    print()'''

# Diamond pyramid
'''n = 5

for i in range(n):
    print(" " * (n-i-1), end="")
    print("* " * (i+1))

for i in range(n-2,-1,-1):
    print(" " * (n-i-1), end="")
    print("* " * (i+1))'''

'''n = 5

for i in range(n):
    print(" " * (n-i-1) + "* " * (i+1))

for i in range(n-1):
    print(" " * (i+1) + "* " * (n-i-1))'''

# Number Pyramid

'''n = 5
for i in range(n):
    print(" " * (n-i-1), end="")
    for j in range(i+1):
        print(j+1, end=" ")

    print()'''

# Inverted number pyramid

'''n = 5
for i in range(n):
    print(" " * i, end="")
    for j in range(n-i):
        print(j+1, end=" ")
    print()'''

# Full Pyramid with Stars.

'''n = 5
for i in range(n):
    print(" " * (n-i-1), end="")
    print("*" * (2*i+1))'''
   
# 
