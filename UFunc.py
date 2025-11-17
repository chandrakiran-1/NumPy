import numpy as np

arr = np.array([1, 2, 3, 4])

# Using some ufuncs
print("Original:", arr)
print("Square:", np.square(arr))
print("Square Root:", np.sqrt(arr))
print("Add 5:", np.add(arr, 5))
print("Multiply by 2:", np.multiply(arr, 2))
print(np.min(arr))
print(np.max(arr))
print(np.sin(arr))