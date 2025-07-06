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

'''n = int(input("Give size of a matrix: "))

for i in range(n):
    for j in range(n):
        if i == j:
            print(1, end=(" "))
        else:
            print(0, end=(" "))
    print()'''


# Python program to check whether a given square matrix is symmetric or not.

'''def is_symmetric(matrix):
    row = len(matrix)
    for i in range(row):
        for j in range(row):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True
    
matrix = [[1, 2, 3],
          [2, 4, 5],
          [3, 5, 6]]

if is_symmetric(matrix):
    print("The matrix is Symmetric.")
else:
    print("The matrix is not Symmetric.")'''


# Python program to check whether a given square matrix is an upper triangular matrix or not.

'''def upper_triangle(matrix):
    row = len(matrix)
    for i in range(row):
        for j in range(row):
            if i > j and matrix[i][j] != 0:
                return False
    return True
            
matrix = [[1, 0, 0],
          [0, 4, 5],
          [0, 0, 6]]

if upper_triangle(matrix):
    print("Given matrix is Upper triangle matrix.")
else:
    print("Given matrix is not a Upper triangle matrix.")'''


# Python program to check whether a given square matrix is a lower triangular matrix or not.

'''n = [[1, 0, 0],
     [2, 3, 0],
     [4, 5, 6]]

n = len(n)
matrix = True

for i in range(n):
    for j in range(n):
        if i < j and n[i][j] != 0:
            print(False)
        else:
            print(True)'''

            
# Determinant of a 2*2 matrix.

'''def determinant_2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
matrix_2 = [[1,2],[3,4]]
result = determinant_2(matrix_2)
print("Determinant of a matrix: ", result)'''


# Determinant of a 3*3 matrix.

'''def determinant_3(matrix):
    # Using cofactor expansion
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[0][2]
    d = matrix[1][0]
    e = matrix[1][1]
    f = matrix[1][2]
    g = matrix[2][0]
    h = matrix[2][1]
    i = matrix[2][2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)
    

matrix_3 = [[1,2,3], [4,5,6], [7,8,9]]
result = determinant_3(matrix_3)
print("Determinant of matrix: ", result)'''


# Check if Matrix is Singular or Non-Singular.

'''def is_singular(matrix):
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return determinant == 0
        
matrix = [[1,2],
          [3,4]]
result = is_singular(matrix)

if result:
    print("It is a singular matrix.")
else:
    print("It is non-singular matrix.")'''



