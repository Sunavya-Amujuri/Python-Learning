## Operations on vectors.

'''a = [1, 2, 3]
b = [4, 5, 6]

#Vector Addition.
add = [a[i] + b[i] for i in range(len(a))]
print(("Addition: "), add)

#Scalar Multiplication.
scalar = 3
scaled = [scalar * x for x in a]
print("Multiplication: ", scaled)

# Dot Product
doct_Product = sum(a[i] * b[i] for i in range(len(a)))
print("Dot Product: ", doct_Product)'''


## Matrix addition

'''A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

result = [[0,0],
          [0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] + B[i][j]

print("Matrix Addition: ")
for row in result:
    print(row)'''

## Matrix Subtraction

'''A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

result = [[0,0],
          [0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] - B[i][j]

print("Matrix Subtraction: ")
for row in result:
    print(row)'''


## Matrix Multiplication

'''A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

result = [[0,0],
          [0,0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

print("Matrix Multiplication: ")
for row in result:
    print(row)'''


## Matrix Transpose

'''A = [[1,2,3],
    [4,5,6]]

transpose = [[0,0],
             [0,0],
             [0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        transpose[j][i] = A[i][j]

print("Matrix Transpose: ")
for row in transpose:
    print(row)'''

# Python Program for Diagonal and Trace:

'''A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

diagonal = []
trace = 0

for i in range(len(A)):
    diagonal.append(A[i][i])
    trace += A[i][i]

print("Matrix Diagonal: ", diagonal)
print("Matrix Trace: ", trace)'''

# Python Program for Diagonal and Trace.

'''A = [[1,2,3,],
     [4,5,6,],
     [7,8,9]]

anti_diagonal = []
trace = 0
n = len(A)

for i in range(len(A)):
    anti_diagonal.append(A[i][n-1-i])
    trace += (A[i][n-1-i])

print("Matrix Anti_matrix: ", anti_diagonal)
print("Anti_diagonal Trace: ", trace)'''


# Write a Python program to print an identity matrix of size n

n = int(input("Give size of a matrix: "))

for i in range(n):
    for j in range(n):
        if i == j:
            print(1, end=(" "))
        else:
            print(0, end=(" "))
    print()

