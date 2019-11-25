import numpy as np

a=[[1,2,3,4,5,6], [1,2,3,4,5,6],[1,1,3,4,5,7]]
print(a)

b=np.array(a)
x=[7,8,9,0,1,3]
a.append(x)
a=np.array(a)
print(a)
print(a[0])
#print(b )
#print(b.max(axis=1))
#print(b.take(0,axis=1))
#print(b.sum(axis=0))