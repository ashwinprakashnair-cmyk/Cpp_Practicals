import numpy as np

# 1D Array operations

# Creating 1D Array

arr1 = np.array([10, 20, 30, 40, 50])
print("The first array is: ", arr1)

# Arranging an array

arr2 = np.arange(1, 11)
print("The arranged array is: ", arr2)

# Implementing linspace 

arr3 = np.linspace(0, 1, 5)
print("Linspace operation: ", arr3)

# 2D Array Operations

# Creating 2D Array

arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
print("\n2D Array:")
print(arr2d)

# 3. Indexing
print("\nIndexing:")
print("\nFirst element of arr1:", arr1[0])
print("Element at row 2, column 3:", arr2d[1, 2])

# 4. Slicing
print("\nSlicing:")
print("Elements from index 1 to 3:", arr1[1:4])
print("First two rows:\n", arr2d[:2])
print("Second column:", arr2d[:, 1])

# 5. Reshaping
arr4 = np.arange(1, 9)
reshaped = np.reshape(arr4, (2, 4))
print("\nReshaped Array (2x4):")
print(reshaped)

# 6. Mathematical Operations
print("\nMathematical Operations:")
print("Sum =", np.sum(arr1))
print("Mean =", np.mean(arr1))

print("Array + 7 =", arr1 + 7)
print("Array * 8 =", arr1 * 8)
