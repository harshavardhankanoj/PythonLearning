import numpy as np
np.set_printoptions(legacy='1.13')
s=input()
lis=list(map(float,s.split()))
array=np.array(lis)
print(np.floor(array))
print(np.ceil(array))
print(np.rint(array))