#%%
import numpy as np

a = np.array([0,1,2,3,4])
b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])
b/2.2
b*a

b[3:5]=111.02, 9.81
b

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
arr[1:8:2]

c = np.array([20, 1, 2, 3, 4])
select = [0, 2, 3, 4]
d=c[select]
d

print(c.size)
print(c.ndim)
print(c.shape)

print(c.mean())
print(c.std())
print(c.max())

a = np.array([0,1,2,3,4])
b = np.array([3,5,7,9,11])
print(np.dot(a, b))
print(np.divide(a, b))
print(np.multiply(a,b))
