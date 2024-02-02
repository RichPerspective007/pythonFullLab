'''

B) Read two matrices and add them. Store the matrices and result in a file.

'''

from random import *
import numpy as np
#creating two 4*4 matrices
matrix1 = np.array([[randint(1,100) for i in range(4)] for j in range(4)])
matrix2 = np.array([[randint(1,100) for i in range(4)] for j in range(4)])

#creating a file to write these matrices
matrixFile = open('MatricesAlternate.txt','a')

newmat = np.ndarray((2,3),dtype=np.int32)
#writing matrix to the file
matrixFile.write(str(matrix1))