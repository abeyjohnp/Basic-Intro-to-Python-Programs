Numerical Python

Numpy arrays are better ways to store than list

# Creating NUMPY arrays

import numpy as np
a=np.array([1,2,3,4,5])
a

> array([1, 2, 3, 4, 5])

import numpy as np
a=np.array([1,2,4])
b=np.asarray(a)
a[1]=3
print(a)
print(b)

>[1 3 4]
>[1 3 4]

in asarray, it points to the same location as the original array, so changes made in original array is reflected in the asarray

np.zeros(5) makes an array of 5 zeroes

np.empty() creates an array without initalising its values to any particular value

np.arange() is similar to an array valued version of range function

np.ones_like(arr) - whatever is the dimension of the arr, say 3 by 5, then it will create a 3 by 5 array filed with ones.

similarly np.zeros_like(arr)

np.eye(4) - makes a square matrix of 4by4

np.identity(4) - makes a 4 by 4 identity matrix 

