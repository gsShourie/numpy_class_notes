
#                       Numpy 101.
# Functions that permit you to define numpy arrays and matrices.

import numpy as np # first, import numpy; alias 'np' is commonly-accepted.


## =================== Array/Matrix/Tensor creation ==========================
print("\n=================== Array creation ======================")

# A matrix of zeros
X = np.zeros((3,2)) # size is passed as a python tuple (3,2)
print("3x2 matrix filled with zeros: \n", X)

# A matrix of ones
X = np.ones((2,3))
print("\n2x3 matrix filled with ones: \n", X)

# An identity matrix
X = np.eye((3)) # Since identity matrix is always square, takes only one size
print("\n3x3 identity matrix: \n", X)

# Random matrix/tensor
X = np.random.rand(3,2,2) # Attention: size is passed as is, not as a tuple
print("\n3x2x2 tensor filled with random numbers: \n", X)

# Direct matrix definition
X = np.array([[1,2,3,4],
              [5,6,7,8]])
print("\nA directly defined matrix: \n", X)



## =================== Data type ==========================
print("\n=================== Data type ==========================")
# All values of a numpy array have a specific data format.
# Examples of formats: int (integer number), float(floating point number),
# uint (unsigned int) and others (https://numpy.org/devdocs/user/basics.types.html).

# Until now, we didn't specify the type of values, so numpy used the default one,
# which is np.float64.

# An integer matrix:
X = np.ones((2,2), dtype=np.int32) # Set all values to be integers
print("Ones matrix (int): \n", X)
print("Type:", X.dtype, "Size: ", X.nbytes) # Returns the size of the matrix in bytes.
                          # Here, the size is equal to four elements times the
                          # size of an int32, which is 32 bits or 4 bytes. So the
                          # total size is 16 bytes.

# A float matrix:
X = np.ones((2,2)) # If you do not specify the type, numpy uses the largest float64.
print("\nOnes matrix (float): \n", X)
print("Type:", X.dtype, "Size: ", X.nbytes)

# Why do you need this? Sometimes np.float64 is simply too large for you. For example,
# in image processing, you need to store values between 0 and 255, which takes only
# one byte. Setting an image (and images are matrices of brightness) to be of np.float64
# will multiply its size by eight! Processing time for such images will also increase.


# A recap on properties of arrays. There is lots of them, but here are the three most
# frequently used:
print("\nProperties")
print('Matrix shape: ', X.shape)
print('Data type: ', X.dtype)
print('Size in bytes', X.nbytes)
# Other np.array properties can be found at https://numpy.org/devdocs/reference/generated/numpy.ndarray.html.


# ================== Accessing single elements ======================
print("================== Accessing single elements ======================")
# Reading an element:
X = np.zeros((3,3))
print("\nSingle element:", X[0][1])

# Writing to an element:
X[0,1] = -1
print("Altered matrix:\n", X)



# ================== Copying of an array ======================
print("\n================== Copying of an array ======================")
# Wrong way of copying an array:
print('A wrong way to make a copy, Y = X: \n')
X = np.zeros((3,3))
Y = X # Makes a "copy" (wrong, it actually creates an alias for X)
Y[1,1] = 1 # Alternate the alias
print("Original:\n", X, '\nCopy:\n', Y)

# Correct way to copy an array
print('\nA correct way to make a copy, Y = np.copy(X): \n')
X = np.zeros((3,3))
Y = np.copy(X) # Actually creates a new matrix in the memory
Y[1,1] = 1 # Alternate the copied matrix
print("Original:\n", X, '\nCopy:\n', Y)



# ================== Concatenation of arrays ==================
print('\n================== Concatenation of arrays ==================')
X = np.zeros((3,3))
Y = np.ones((2,3))
Z = np.ones((3,2))
print('Vertical concatenation:\n', np.concatenate((X,Y), axis=0))
print('Horizontal concatenation:\n', np.concatenate((X,Z), axis=1))

# Here, argument axis specifies along which dimension to concatenate the matrices:
# axis=0 is default and concatenates along the vertical axis, which in numpy considered
# the first; axis=1 is for horizontal axis, and so on.
