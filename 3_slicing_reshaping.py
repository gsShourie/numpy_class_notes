# Numpy 101
# Slicing and reshaping of numpy arrays
import numpy as np

# ============= Slicing a multidimensional array ==============
X = np.random.randint(-3, 3, size=(3,3))
print('\nFull matrix X :\n', X)
print('\nA vertical slice (first column) X[:,0] :\n', X[:,0])
print('\nA horizontal slice (first row)  X[0,:] :\n', X[0,:])

# ============= Sub-arrays =============
X = np.random.randint(-3, 3, size=(3,3))
print('\nFull matrix X :\n', X)
print('\nA top-left 2x2 sub array X[0:2,0:2] :\n', X[0:2,0:2])
# Attention on how the last element is not included.
# 0:2 actually returns the 0-th and 1-st elements, but not the 2nd one.

# ============= Conditional access, masks =============
X = np.random.randint(-3, 3, size=(3,3))
M = X < 0 # Get a boolean mask
print('\nMatrix X :\n', X)
print('\nMask M = X < 0 :\n', M)

# You now use mask to alter the X, for example:
X[M] = 0
print('\nX after applying the mask X[M]=0 :\n', X)

# You can, of course, merge two steps into one:
X[X < 0] = 0
# Important: mask should be of the same shape as X.

# ============= Reshaping =============
X = np.random.randint(-3, 3, size=(3,4))
print('\nMatrix X :\n', X)
print('\nX transformed to a 1x12 array :\n', X.flatten()) # Used when you want to write a matrix to a file or a serial port
print('\nX transformed to a 6x2 matrix :\n', X.reshape((6,2))) # Used in all kinds of situations
#print('\nX transformed to a 6x2 matrix :\n', X.reshape((6,-1)))
# -1 tells numpy to calculate the second dimension itself from
# from the size of the original matrix

# ============= Transposition =============
X = np.random.randint(-3, 3, size=(2,3))
print('\nMatrix X :\n', X)
print('\nMatrix X transposed :\n', X.transpose())
