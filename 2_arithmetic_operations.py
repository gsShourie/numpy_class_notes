# Numpy 101
# Basic arithmetic operations on numpy arrays.
import numpy as np

# Matrix and a scalar
print('\nSum of matrix and a scalar.\n')
X = np.zeros((3,3))
print('\nScalar is added to each element of the matrix:\n', X + 1)
print('This applies to all other arithmetic operations.')

# Matrix and a vector
X = np.zeros((3,3))
y = np.array([[1,2,3]]) # Attention, double brackets to make it a
                        # (1,3) but not a (3,)!
print('\nInitial matrices:\n', 'X=', X, '\ny=', y)
print('\n3x3 + 1x3:\n', X + y)
print('\n3x3 + 3x1:\n', X + y.transpose())

# Matrix and a matrix, element-wise operations
X = np.ones((3,3))
Y = np.eye(3)
print('\nMatrix (*) matrix, element-wise:\n', X * Y)
# For element-wise operations, matrices should be of the same size!

# Matrix multiplication
X = np.ones((4,3))
Y = np.eye(3)
print('\nMatrix * matrix, matrix product:\n', np.dot(X,Y))
# By definition, first matrix has to have the same numbers of columns as
# the number of row in the second matrix.
