"""Tensors"""

import numpy as np
import torch

data = [[1, 2], [3, 4]]
x_data = torch.tensor(data)

x_data
data

np_array = np.array(data)
x_np = torch.from_numpy(np_array)
x_np


x_ones = torch.ones_like(x_data)  # retains the properties of x_data
print(f"Ones Tensor: \n {x_ones} \n")

x_rand = torch.rand_like(x_data, dtype=torch.float)  # overrides the datatype of x_data
print(f"Random Tensor: \n {x_rand} \n")

x = x_data

x.shape
x.dtype
x.device

tensor = torch.ones(4, 4)
print(f"First row: {tensor[0]}")
print(f"First column: {tensor[:, 0]}")
print(f"Last column: {tensor[..., -1]}")
tensor[:, 1] = 0
print(tensor)

t1 = torch.cat((x, x))
x
t1

y = t1 @ t1.T
y
agg = y.sum()
agg.dtype

agg.item()
type(agg.item())

x

x.add(5)
x
x.add_(5)
x

# shouldn't be used, as memory is lost

# A bridge with numpy

t = torch.ones(5)
print(f"t: {t}")
n = t.numpy()
print(f"n: {n}")


t.add_(1)
print(f"t: {t}")
print(f"n: {n}")
