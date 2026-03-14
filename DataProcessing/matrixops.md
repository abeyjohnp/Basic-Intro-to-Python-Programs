just write a+b,a-b etc..
it undergoes element wise operation

# OPS WITH SCALARS
a*5

# SLICING
a[5],a[5:8]
But this is a duplicate list which is seperate
but if we use a_slice=a[3:5]
and change a_slice of 1 index.

> arr[:2,1:]
This actually means that we select the first 2 rows, and the coloumns from the coloumn 1, so which are the common rows and coloumns they are selected.

# NORMAL MATRIX MULTIPLICATION

np.dot(a,b)
np.matmul(a,b)

# STATISTICAL FUNCTIONS
x=np.array(arr)
x.max()
x.min()
x.sum()
x.sum(axis=0)
argmin,argmax to get the index of the min and max


# MATRIX TRANSPOSE
x.transpose() 

# RANDOM NUMBER GENERATION

numpy.random.normal(size=(4,4)) - random numbers generated from this normal distribution

np.random.uniform - uniform distribution
similary there is gamma, beta

np.random.randint