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

np.arange(
    8,
)

np.arange(8, 12)

np.linspace(0, 10, num=5)

# Adding, removing, and sorting elements

x = np.ones(2, dtype=np.int64)

arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])

y = np.sort(arr)

np.concatenate((y, x))  # This works of course

long = np.concatenate((x, x, x, x))
long.shape
# This also works and the shape is (8,) whatever that means
y.shape
# y has the same shape
np.concatenate((y, long))
# this works and makes a very long array
# shape is (16,)

y2 = [y]
long2 = [long]
dimes = np.concatenate((y2, long2), axis=0)
# if i do this suddenly they get turned into a 2D array
dimes.shape

# This turns them into python lists, and then they concat differently for some reason


# How do you know the shape and size of an array?
array_example = np.array(
    [
        [[0, 1, 2, 3], [4, 5, 6, 7]],
        [[0, 1, 2, 3], [4, 5, 6, 7]],
        [[0, 1, 2, 3], [4, 5, 6, 7]],
    ]
)
array_example.ndim
array_example.size
array_example.shape

long.reshape(2, 4)

y.reshape(2, 4)

standard = np.arange(24)
new = standard
print(new)
new = new.reshape(2, 4, 3)
print(new)
# this is pretty cool


# How to convert a 1D array into a 2D array (how to add a new axis to an array)
a = np.array([1, 2, 3, 4, 5, 6])
a.shape
print(a)

a2 = a[np.newaxis, :]
a2.shape

print(a2)

row_vector = a[np.newaxis, :]
row_vector.shape


col_vector = a[:, np.newaxis]
col_vector.shape

print(col_vector)
print(row_vector)

# this is kind of weird
# we create ob

ob = np.array([1, 2, 3, 4, 5, 6])
print(ob)
ob.shape
# then we do
ob[np.newaxis, :].shape
ob[np.newaxis, :]

ob[:, np.newaxis]
ob[:, np.newaxis].shape
# ok, I think i kind of get it.


# Indexing and slicing

data = standard
data[1]
data[0:2]
data[1:]
data[-2:]

data[1:12]

data = data.reshape(6, 4)
data[1:6, 0:2]

print(data[data < 12])
data.shape
con = data > 8
print(data[con | (data == 3)])
print(data[con & (data == 12)])
print(data)
print(np.nonzero(data > 20))

# ok this is actually pretty cool. I like numpy now


# zipping

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
b = np.nonzero(a < 5)
print(b)

list_of_coordinates = list(zip(b[0], b[1]))
print(list_of_coordinates)

for coord in list_of_coordinates:
    print(coord)

print(a[b])


# How to create an array from existing data
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
arr1 = a[3:8]
print(arr1)

a1 = np.array([[1, 1], [2, 2]])

a2 = np.array([[3, 3], [4, 4]])


arr2 = np.hstack((a1, a2))
arr3 = np.vstack((a1, a2))
print(arr2)

print(arr3)

x = standard.reshape(2, 12)
print(x)

y = np.hsplit(x, (3, 4))
print(y)

# on views

a = standard.reshape(4, 6)
print(a)

b1 = a[0, :]
print(b1)

b1[0] = 99
b1 = 44  # This doesn't modify a. Makes sense

b2 = a.copy()
b2[2] = 22
b2

a
