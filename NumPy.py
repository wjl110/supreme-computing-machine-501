import numpy as np

# Create a 1D array
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.zeros(5)  
arr3 = np.ones((3, 3))
arr4 = np.arange(0, 10, 0.5)
arr5 = np.linspace(0, 1, 5)

print(arr1 * 2)
print(arr1 + arr2)
print(np.sqrt(arr1))
print(np.exp(arr1))