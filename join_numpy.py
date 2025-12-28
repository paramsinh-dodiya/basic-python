import numpy as np 

# vertically stack 

n1=np.array([10,20,30])
n2=np.array([40,50,60])
n3=np.vstack((n1,n2))
print(n3)
print()

# horizontal stack

n4=np.array([10,20,30])
n5=np.array([40,50,60])
n6=np.hstack((n4,n5))
print(n6)
print()

#column stack 

n7=np.array([10,20,30])
n8=np.array([40,50,60])
n9=np.column_stack((n7,n8))
print(n9)

