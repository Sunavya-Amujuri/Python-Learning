# 1. Diamond pattern

'''n = 5
for i in range(n):
    print(" " * (n-i-1), end="")
    print("* " * (i+1))
for i in range(n-2,-1,-1):
    print(" " * (n-i-1), end="")
    print("* " * (i+1))'''

# or

'''n = 5

for i in range(n):
    print(" " * (n-i-1) + "* " * (i+1))

for i in range(n-1):
    print(" " * (i+1) + "* " * (n-i-1))'''

# 2. Hollow Pyramid

'''n = 5
for i in range(n):
    print(" " * (n-i-1), end="")
    print("*" * (2*i+1))'''

# 3. only middle and colume hollow pattern
'''n = 5
for i in range(n):
    for j in range(n):
        if (i == n//2 or j == n//2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()'''

# 4. Right and left diagonal hollow pattern
'''n = 5
for i in range(n):
    for j in range(n):
        if (i == j or i+j == n-1):
            print("*", end="")
        else:
            print("  ", end="")
    print()'''

# 5. Hollow square pattern.
'''n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or  j == 0 or j == n-1 :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()'''

# 6. Hollow increasing triangle.

'''n = 5
for i in range(n):
    for j in range(i+1):
        if (i == n-1 or j == 0 or j == i):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()'''

# 7.Inverted hollow triangle.

'''n = 5
for i in range(n):
    for j in range(n-i):
        if (i == 0 or j == 0 or j == n-i-1):
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()'''

# 8.Hollow Hill pattern.
'''n = 5
for i in range(n):
    print("  " * (n-i), end = "")
    for j in range(2*i+1):
        if ( i == n-1 or j == 0 or j == 2*i ):
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()'''

# 9.Hollow Diamond pattern

'''n = 5
for i in range(n):
    print("  " * (n-i-1), end = "")
    for j in range(2*i+1):
        if ( j == 0 or j == 2*i):
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()

for i in range(n-2,-1,-1):
    print("  " * (n-i-1), end = "")
    for j in range(2*i+1):
        if ( j == 0 or j == 2*i):
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()'''

# 10.Hour glass pattern (centered, vertical shrinking)

'''n = 5
for i in range(n):
    for j in range(i):
        print(" ", end = " ")
    for j in range(2*(n-i)-1):
        print("*", end = " ")
    print()

for i in range(1, n):
    for j in range(n-i-1):
        print(" ", end = " ")
    for j in range(2 * i + 1):
        print("*", end = " ")
    print()'''

# or

'''n = 5
for i in range(n):
    print("  " * i, end = "")
    print("* " * (2*(n-i)-1), end = "")
    print()

for i in range(1, n):
    print("  " * (n-i-1), end = "")
    print("* " * (2 * i + 1), end = "")
    print()'''

# 11.Mirrored Hourglass (horizontal shrinking).

'''n = 5
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    for j in range(2 * (n - i - 1)):
        print(" ", end = " ")
    for j in range(i+1):
        print("*", end=" ")
    print()

for i in range(n-2, -1, -1):
    for j in range(i+1):
        print("*", end=" ")
    for j in range(2 * (n - i - 1)):
        print(" ", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()'''
   
# or 

'''n = 5
for i in range(n):
    print("* " * (i+1), end=" ")
    print("  " * (2*(n-i-1)), end="")
    print("* " * (i+1),end=" ")
    print()

for i in range(n):
    print("* " * (n-i-1), end=" ")
    print("  " * (2*(i+1)), end="")
    print("* " * (n-i-1), end=" ")
    print()'''

# Alphabetical shape Pattern

# 12.A letter

'''n = 7
for i in range(n):
    for j in range(5):
        if((j==0 or j==4) and i!=0) or ((i==0 or i==3) and (j>0 and j<4)):
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()'''

# 13. B letter

'''n = 7
for i in range(7):
    for j in range(5):
        if ((j == 0) or (j == 4 and (i!=0 and i!=3 and i!=6)) or (i == 0 or i == 3 or i == 6) and (j>0 and j<4)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()'''

# 14. C letter
'''n = 7
for i in range(7):
    for j in range(5):
        if (j == 0) and (i!=0 and i!=6 ) or ((i == 0 or i == 6) and (j>0)):
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()'''

# 15. D letter

'''n = 7
for i in range(7):
    for j in range(5):
        if ((j == 0) or ((j == 4) and (i !=0 and i!= 6))  or ((i == 0 or i == 6) and (j>0 and j<4))):
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()'''

# 16. G letter

'''n = 7
for i in range(n):
    for j in range(6):
        # if (j == 0) or ((i == 0 or i == 6) and (j>0 and j<5)) or ((j == 4) and (i>3)) or (i==3 and j>2):
        if j == 0 or (j==4 and i!=1 and i!=2) or ((i==0 or i==6) and (j>0 and j<4)) or (i==3 and (j>2)):
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()'''

# 17. K letter

'''n = 7
for i in range(n):
    for j in range(5):
        # if j == 0 or (i+j==4 and i<4) or( i-j==2 and i>=4):
        if j == 0 or j == 4 - i or j == i - 2:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()'''

# 18. M letter

'''n = 7
for i in range(n):
    for j in range(n):
        if (j==0 or j==6) or (i==j and i>0 and j<4)or ((j==6-i) and i>0 and i<3) :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()'''

# 19. N letter

'''n = 7
for i in range(n):
    for j in range(n):
        if (j==0 or j==n-1) or (i==j and j>0 and j<n-1) :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print() ''' 

# 20. Q letter

'''n = 8
for i in range(n):
    for j in range(5):
        if ((j==0 or j==4) and (i>0 and i<6)) or ((i==0 or i==6) and j>0 and j<4) or (i==5 and j==1) or (i==7 and j==3):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()'''

# 21. S letter

'''n = 7
for i in range(n):
    for j in range(5):
        if (j==0 and i>0 and i<3) or ((i==0 or i==3 or i==6) and (j>0 and j<4)) or (j==4 and i>3 and i<6):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()'''

# 22. Word "Python" in right triangle pattern.

'''str = "Python"
length = len(str)

for i in range(length):
    for j in range(i+1):
        print(str[j], end = " ")
    print()'''

#23. 2 formats by using numbers

n = 6
for i in range(n-1):
    for j in range(1, n-i):
        print(j, end=" ")
    print()

# or

n = 5
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

n = 5
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(i, end=" ")
    print()


        

            





  

