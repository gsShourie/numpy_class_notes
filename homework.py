# Don't forget to import the package
import numpy as np
# Using numpy, contruct the following matrices:

# a)
# A =   [[   0.,    0.,    0.],
#       [   0.,    0.,    0.],
#       [   0.,    0., 1000.]]
A=np.zeros([3,3])
A[2,2]=1000
print(A)

# b)
# B =   [[1., 0., 0.],
#       [0., 1., 0.],
#       [0., 0., 1.],
#       [1., 0., 0.],
#       [0., 1., 0.],
#       [0., 0., 1.]]
B=np.eye(3)
B=np.concatenate((B,B),axis=0)
print(B)

# c)
# C =   [[ 1.,  0.,  0.],
#        [ 0.,  1.,  0.],
#        [-1.,  5.,  0.],
#        [-1.,  0.,  5.]]
C=np.array([[1,0,0],[0,1,0],[-1,5,0],[-1,0,5]])
C=C.astype(float)
print(C)

# d) Reshape C to get the following:
# D =   [[ 1.,  0.,  0.,  0.],
#       [ 1.,  0., -1.,  5.],
#       [ 0., -1.,  0.,  5.]]
D=C.reshape((3,4))
print(D)


# e) ... and the following:
# E =   [[ 1.,  0., -1., -1.],
#       [ 0.,  1.,  5.,  0.],
#       [ 0.,  0.,  0.,  5.]]


# f) In matrix E, increment all elements (add 1)
#    that are larger than 0.
E=np.copy(D)
E[E>0]=E[E>0]+1
print(E)

# g) Set all elements of the first row in E to 0.
E[0,:]=0
print(E)

# h) Set all elements of the right half of E to 1.
E[:,2:4]=1
print(E)

# i) Get rid of the floating point part in the elements of E (round them to integers)
E=E.astype(int)         #we could use np.rint to round the input to nearest integers
print(E)                #but that would not help us get rid of the floating point

# j) Can you get a matrix product np.dot(D,E)?
#    If not, what simplest transformation you need to
#    apply to one of the matrices to make the product
#    possible? Provide results of applying that transform
#    to either of the matrices.

#Answer= No. We can transpose D to make the multication possible
D=D.transpose()
print(np.dot(D,E))
#
