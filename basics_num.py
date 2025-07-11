import numpy as np

# Array basics

a = np.array([[1, 2, 8], [3, 4, 5]])

print(a)

a.shape


a[0]


a.ndim


b = np.array([[[1, 2, 8], [3, 4, 5]], [[2, 8, 3], [4, 5, 6]]])
b.shape

b.ndim
print(len(b.shape) == b.ndim)


a.size


# Creating arrays

c = np.zeros((2, 3))
print(c)

np.empty((2, 6))


x = np.ones(2, dtype=np.int64)

print(x)
