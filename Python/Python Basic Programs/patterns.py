## Square of stars

# 1. Solid Square of Stars.

'''n = 5
for i in range(n):
    for j in range(n):
        print("#", end = "")
    print()'''

#  2. Hollow Square. Print stars only on the border — space inside

'''n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("#", end = " ")
        else:
            print("*", end = " ")
    print()'''

#  3. Number Square. Same square layout, but use numbers instead of *.

'''n = 5
for i in range(n):
    for j in range(n):
        print (j+1, end = " ")
    print()'''

# 4. Alphabet Square. Like number square, but with alphabets.

'''n = 6
for i in range(n):
    for j in range(n):
        print(chr(65 + j), end = " ")
    print()'''

#  5. Reverse Square (Numbers / Alphabets). You can also print numbers in reverse:

'''n = 4
for i in range(n):
    for j in range(n, 0, -1):
        print(j, end=" ")
    print()'''

# Left-Aligned Triangle Pattern Programs.
# 1. Basic Star Triangle.

'''n = 5
for i in range(1, n+1):
    print("* " * i)'''

# or

'''n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        print("*", end = " ")
    print()'''

#  2. Number Triangle (Ascending 1 to i)

'''n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end = " ")
    print()'''

# 3. Row Number Triangle (same number in a row).

'''n = 5
for i in range(1, n+1):
    print((str(i) + " ") * i)'''

# 4. Continuous Number Triangle.

'''n = 5
num = 1
for i in range(1, n+1):
    for j in range(i):
        print(num, end = " ")
        num += 1
    print()'''

# 5. Alphabet Triangle (A, AB, ABC)

'''n = 5
for i in range(1, n+1):
    for j in range(i):
        print(chr(65 + j), end = " ")
    print()'''

# or 

'''n = 5
num = 0
for i in range(1, n+1):
    for j in range(i):
        print(chr(65 + num), end = " ")
        num += 1
    print()'''
    

# 6. Alphabet Triangle (AAA, BBB).

'''n = 5
for i in range(0, n):
    print((chr(65 + i) + " ") * (i+1))
print()'''


# 7. Binary Pattern (alternating 0, 1 row-wise)

'''n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        print ((i+j)%2, end = " ")
    print()'''

#  8. Odd Number Triangle.

'''n = 5
num = 1
for i in range(1, n+1):
    for j in range(i):
        print(num, end = " ")
        num += 2
    print()'''

# 9. Even Number Triangle

'''n = 6
num = 2
for i in range(1, n+1):
    for j in range(i):
        print(num, end = " ")
        num += 2
    print()'''

# 10. Reverse Row Number Triangle.

'''n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print(i, end = " ")
    print()'''

# 11.  try Inverted Left-Aligned Triangle.

'''n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end = " ")
    print()'''


## Right-Aligned Triangle

# 1. Right-Aligned Star Triangle

'''n = 5
for i in range(1, n+1):
    print(" " * (n-i) + "*" * i)
print()'''

# 2. Right-Aligned Number Triangle.

'''n = 5
for i in range(1, n+1):
    print(" " * (n-i), end = " ")
    for j in range(1, i+1):
        print(j, end = "")
    print()'''

# 3. Right-Aligned Same Number in Row.

'''n = 5
for i in range(1, n+1):
    print(" " * (n-i) + str(i) * i)'''

# 4. Right-Aligned Alphabet Triangle.

'''n = 5

for i in range(1, n+1):
    print(" " * (n-i), end = "")
    for j in range(i):
        print(chr(65 + j), end = "")
    print()'''

# 5. Right-Aligned Reverse Number Triangle.

'''n = 5
for i in range(n, 0, -1):
    print(" " * (n-i), end = "")
    for j in range(n, n-i, -1):
        print(j, end = "")
    print()'''

# 6. Right-Aligned Inverted Star Triangle.

'''n = 5
for i in range(n):
    print(" " * i + "*" * (n-i))'''

# 7. Continuous Right-Aligned Number Triangle.

'''n = 5
num = 1
for i in range(1, n+1):
    print("  " * (n-i), end = "")
    for j in range(i):
        print(f"{num:2}", end =" ")
        num += 1
    print()'''

# 8. Right-Aligned Reverse Alphabet Triangle.

'''n = 5
for i in range(1, n+1):
    print(" " * (n-i), end = "")
    for j in range():'''


   

    
       

           