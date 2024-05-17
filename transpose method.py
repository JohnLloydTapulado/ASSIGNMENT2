

#example1
import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])
print(A)


B = A.transpose()
print(B)

#example2

import numpy as np

A = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print(A)


B = A.transpose()
print(B)

#EXAMPLE3
import numpy as np

A = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])
print(A.shape)


B = A.transpose((2, 0, 1))
print(B.shape)