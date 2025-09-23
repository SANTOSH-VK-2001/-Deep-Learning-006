import numpy as np
print("Matrix Calculator")
print("Numpy version:", np.__version__)
print("Give me Dimensions of the Matrix (rows, columns): ")
m1 = int(input("Rows first matrix: "))
n1 = int(input("Columns first matrix: "))
a = np.zeros((m1, n1))
print("Enter the elements of the first matrix:")
for i in range(m1):
    for j in range(n1):
        print("Element [", i, ",", j, "] : ", end="")
        value = int(input())
        a[i, j] = value
print("First matrix:")
print(a)
m2 = int(input("Rows second matrix: "))
n2 = int(input("Columns second matrix: "))
b = np.zeros((m2, n2))
print("Enter the elements of the second matrix:")
for i in range(m2):
    for j in range(n2):
        print("Element [", i, ",", j, "] : ", end="")
        value = int(input())
        b[i, j] = value
print("Second matrix:")
print(b)
print("Choose the operation you want to perform:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
choice = int(input("Enter your choice (1/2/3): "))
if choice == 1:
    if m1 == m2 and n1 == n2:
        result = a + b
        print("Result of Addition:")
        print(result)
    else:
        print("Error: Matrices must have the same dimensions for addition.")
elif choice == 2:
    if m1 == m2 and n1 == n2:
        result = a - b
        print("Result of Subtraction:")
        print(result)
    else:
        print("Error: Matrices must have the same dimensions for subtraction.")
elif choice == 3:
    if n1 == m2:
        result = np.dot(a, b)
        print("Result of Multiplication:")
        print(result)
    else:
        print("Error: Incompatible matrix dimensions for multiplication.")
else:
    print("Invalid choice.")