
### Linear Algebra
Linear Algebra is the branch of mathematics that deals with vectors, matrices, and linear transformations.
It studies how mathematical objects like vectors and matrices can be added, scaled, and transformed using linear equations.

In simple words:
Linear algebra is used to understand and work with:
- Lines
- Planes
- Higher-dimensional data
… using mathematical operations like addition, multiplication, dot products, etc.

Real-world Use:
It's the foundation of:
- Machine Learning & AI
- Computer Graphics
- Data Science
- Robotics
- Engineering

### Vector
A vector is an ordered list of numbers.
It represents:
- A point in space (geometry)
- A set of values (data/features)

Type	        Example
Row Vector	    [1, 2, 3]
Column Vector	[[1], [2], [3]]

## Vector Adition : add = [a[i] + b[i] for i in range(len(a))]

## Scalar Multiplicaion : scaled = [scalar * x for x in a]

## Dot Product : dot_product = sum([a[i] * b[i] for i in range(len(a))])



| Feature           | `[ ]` → List Comprehension             | `( )` → Generator Expression  |

| **Applies to**    | Any iterable operation (math, string, file, etc.) | Any iterable operation|
| **When used**     | When you want results **immediately**  | When you want to **loop later or save memory** 	Creates a generator (lazy, saves memory) |
| **Result Type**   | List                                   | Generator object          |
| **Can be reused?**| Yes                                    | No (can be used only once)    |
| **Speed**         | Faster for small data                  | Better for **large data** or files   |


### Matrix
A matrix is a 2D arrangement of numbers in rows and columns.
- In matrix simply print statement i.e, print("Matrix Addition:") is not enough because it gives the 
  result but in single line, not like a neat matrix.
  So, we also use (for row in result:  and  print(row) ) statements.Where each row is printed on a new line, which looks like a proper matrix format. Easier to read, especially for large matrices.

  print("Matrix Addition:")       # Step 1: Print a heading/title

for row in result:              # Step 2: Loop through each row of the matrix
    print(row)                    # Step 3: Print each row


Variable	          What it loops through	          Why
i	                  Rows of matrix	              len(A)
j	                  Columns in each row	          len(A[0])

This ensures you cover all elements in the matrix using A[i][j].

# Transpose : 
The transpose of a matrix means flipping it over its diagonal — that is, rows become columns and columns become rows.


# Diagonal Elements in a Square Matrix:
For a square matrix, diagonal elements are the ones where the row index = column index, i.e., A[i][i].
Diagonal elements: A[0][0] , A[1][1] , A[2][2] 

# Trace of a Matrix:
The trace is the sum of diagonal elements.

# Anti-Diagonal:
In a square matrix, the anti-diagonal consists of the elements from the top-right to bottom-left.

That means: A[i][n - 1 - i], where n is the number of columns.

# Identity Matrix
An identity matrix is a square matrix in which all the elements of the principal diagonal are 1, and all other elements are 0.

It acts like the number 1 in matrix multiplication:

If A is any matrix, then 𝐴 × 𝐼 = 𝐴

Important Properties and Formulas
Concept	Formula / Description
Multiplicative Identity	
| **Concept**               | **Formula/Description**                                                  |

|**Multiplicative Identity**|$A \times I = I \times A = A$ <br> (*for any matrix A of compatible dimensions*)|
| **Diagonal Elements**     | $I[i][i] = 1$ <br> (*All diagonal elements are1*)                       |
| **Off-Diagonal Elements** | $I[i][j] = 0$ for $i \ne j$ <br> (*All off-diagonal elements are 0*)    |
| **Determinant**           | $\text{det}(I_n) = 1$                                                   |
| **Transpose**             | $I^T = I$ <br> (*Transpose of identity matrix is same as original*)     |
| **Inverse**               | $I^{-1} = I$ <br> (*Inverse of identity matrix is itself*)              |
| **Eigenvalues**           | All eigenvalues of $I$ are **1**                                        |


| Type of Output    | Where to Put `print()`     |
| ----------------- | -------------------------- |
| Matrix/Grid       | Outside inner loop ✅       |
| List on one line  | Inside loop with `end=" "` |
| Pattern/Triangle  | Outside inner loop ✅       |
| One item per line | Inside loop                |


# Symmetric Matrix
A symmetric matrix is a square matrix that is equal to its transpose. In other words, a matrix 
A is symmetric if: A = A^T. This means Aij = Aji
​

