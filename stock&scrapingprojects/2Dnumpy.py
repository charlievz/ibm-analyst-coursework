#%% 
import numpy as np
import matplotlib.pyplot as plt

a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
A = np.array(a)

print(A.ndim, A.shape, A.size, sep="\n")
A[2][1:3]

#%%