
#example 1
import numpy as np

A = np.array([[1, 2], [3, 4]])

# Introduce some floating point error
A[0, 0] = 1.000001
A[0, 1] = 2.000001
A[1, 0] = 3.000001
A[1, 1] = 4.000001

inv_A = np.linalg.inv(A)
print(inv_A)