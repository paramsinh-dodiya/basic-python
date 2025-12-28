import numpy as np

#difference between two arrays


n1=np.array([1,2,3,4,5])
n2=np.array([4,5,6,7,8])
n3=np.setdiff1d(n1,n2)
print(n3)
print()

n4=np.array([1,2,3,4,5])
n5=np.array([4,5,6,7,8])
n6=np.setdiff1d(n5,n4)
print(n6)

# in above unic values has been count