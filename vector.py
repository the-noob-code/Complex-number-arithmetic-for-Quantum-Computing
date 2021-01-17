from complex import *
import numpy as np

def init_vector(dim):
	vector=list()
	for i in range(dim):
		real=float(input("Real part:"))
		imaginary=float(input("Imaginary part:"))
		vector.append(compleX(real,imaginary))
	return np.array(vector)	

def init_matrix(dim1,dim2):
	matrix=list()
	for i in range(dim2):
		i=init_vector(dim1)
		matrix.append(i)
	return np.array(matrix)	

def add_vector(vector1,vector2):
	return vector1+vector2		

def add_matrix(matrix1,matrix2):
	return matrix1+matrix2

def inv_vector(vector):
	for i in vector:
		i.real=i.real*-1
		i.imaginary=i.imaginary*-1
	return vector

def inv_matrix(matrix):
	new_matrix=list()
	for i in matrix:
		new_matrix.append(i*compleX(-1,0))
	return np.array(new_matrix)
		
def srm_vector(vector,scalar):
	return 	vector*scalar

def srm_matrix(matrix,scalar):
	return matrix*scalar

def dot(vector1,vector2):
	inner=compleX(0,0)
	for i,j in zip(vector1,vector2):
		inner+=i*j
	return inner

def action(vector,matrix): 
	li=list()
	for i in matrix.T:
		li.append(dot(i,v1))
	return np.array(li)			

print("----------------Complex Vector Spaces----------------")
v1=init_vector(int(input("Enter dimension for vector1:")))
v2=init_vector(int(input("Enter dimension for vector2:")))
print("Addition=",add_vector(v1,v2))
print("Additive Inverse=",inv_vector(v1))
print("Enter a scalar:")
r=float(input("Real:"))
i=float(input("Imaginary:"))
num=compleX(r,i)	
print("Multiplication by scalar=",srm_vector(v2,num))
print("Matrix 1:")
m1=init_matrix(int(input("Enter m:")),int(input("Enter n:")))
print("Matrix 2:")
m2=init_matrix(int(input("Enter m:")),int(input("Enter n:")))
print("Addition=",add_matrix(m1,m2))
print("Additive Inverse=",inv_matrix(m1))
print("Enter a scalar:")
r=float(input("Real:"))
i=float(input("Imaginary:"))
num=compleX(r,i)	
print("Multiplication by scalar=",srm_matrix(m2,num))
print("Vector matrix product=",action(v1,m1))
print("Inner product=",dot(v1,v2))


