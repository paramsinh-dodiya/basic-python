import numpy as np

n1=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(n1)
print("shape of array : ",n1.shape)

print()

n2 = np.array([[1,2,3,4],[4,3,2,1]])
print(n2)

print()

n2.shape = (4,2)    #convert (2,4) matrix in to (4,2) matrix
print(n2)
print()

n2.shape = (8,1)    #convert in (8,1) matrix
print(n2)