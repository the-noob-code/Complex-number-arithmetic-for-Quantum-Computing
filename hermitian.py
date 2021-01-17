from vector import *
import numpy as np

def hermitian(matrix):
	if matrix.all()==matrix.H.all():
		print("Hermitian Matrix")
	else:
		print("Not Hermitian Matrix")	

def unitary(matrix):
	mat=np.matmul(matrix,matrix.H)
	if mat.all()==np.eye(matrix.ndim).all():
		print("Unitary Matrix")
	else:
		print("Not Unitary Matrix")

def tensor(matrix1,matrix2):
	n,m=matrix1.shape
	li=list()
	for i in range(n):
		for j in range(m):
			li.append(srm_matrix(matrix2,matrix1[i,j]))
	return np.array(li)		

print("---------------------Hermitian Matrices/Unitary Matrices/Tensor product---------------------")
m1=init_matrix(int(input("Enter m:")),int(input("Enter n:")))
hermitian(np.matrix(m1))
m2=init_matrix(int(input("Enter m:")),int(input("Enter n:")))
unitary(np.matrix(m2))
print("Tensor product=",tensor(m1,m2))