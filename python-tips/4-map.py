things = [1, 2, 3, 4, 5]

squared = []

for i in things:
    squared.append(i**2)

print(squared)

squared_better = list(map(lambda x: x**2, things))

print(squared_better)

# %%


def multiply(x):
    return x * x


def add(x):
    return x + x


funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)

# %%
