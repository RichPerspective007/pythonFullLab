'''

B) Read two matrices and add them. Store the matrices and result in a file.

'''

from random import *
import numpy as np

#function to read from file
def read_from_file(fileobject):
    ret_mat = []
    for line in fileobject:
        if len(line) < 2:
            break

        line = line[:-1].strip()
        row = list(map(int,line.split(' ')))
        ret_mat.append(row)
    return ret_mat

#function to write to file.
def write_to_file(fileobject,matrix):
    for i in range(4):
        for j in range(4):
            fileobject.write(f'{matrix[i,j]} ')
        fileobject.write('\n')





#creating two 4*4 matrices
matrix1 = np.array([[randint(1,100) for i in range(4)] for j in range(4)])
matrix2 = np.array([[randint(1,100) for i in range(4)] for j in range(4)])

#creating a file to write these matrices
matrixFile = open('Matrices.txt','a')

#writing matrix to the file
write_to_file(matrixFile,matrix1)

matrixFile.write('\n')

write_to_file(matrixFile,matrix2)

matrixFile.close()

#reading the matrices from the file.
matrixFile = open('Matrices.txt','r')
addMatrix1 = read_from_file(matrixFile)
addMatrix2 = read_from_file(matrixFile)

#done with this file for now, so closing it.
matrixFile.close()

#creating two numpy arrays for the matrix.
addMatrix1 = np.array(addMatrix1)
addMatrix2 = np.array(addMatrix2)

#opening a new file to write the matrices and sum result to.
matrixFile = open('Matrices and sum results.txt','a+')

#writing the matrices in question
matrixFile.write('First Matrix: \n')
write_to_file(matrixFile,addMatrix1)

matrixFile.write('\nSecond Matrix: \n')
write_to_file(matrixFile,addMatrix2)

#creating a 4*4 matrix to store the sum and initialising it with zeros
sumMatrix = np.zeros((4,4),dtype=np.int32)

matrixFile.write('\n\nSum of the matrices Matrix: \n')
for i in range(4):
    for j in range(4):
        sumMatrix[i,j] = addMatrix1[i,j] + addMatrix2[i,j]

#writing the result to the file
write_to_file(matrixFile,sumMatrix)
matrixFile.close()

