#exanple1
import numpy as np

A = np.array([[1, 2], [3, 4]])

det_A = np.linalg.det(A)
print(det_A)

#example2
import numpy as np

A = np.array([[1, 2], [0, 3]])

det_A = np.linalg.det(A)
print(det_A)


#example3
import numpy as np

A = np.array([[1, 0], [0, 1]])

det_A = np.linalg.det(A)
print(det_A)