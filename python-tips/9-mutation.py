foo = ["hi"]
print(foo)

bar = foo
bar += ["bye"]

print(foo)

print(bar)

# %%


def add_to(num, target=[]):
    target.append(num)
    return target


add_to(1)
# Output: [1]

add_to(2)
# Output: [1, 2]

add_to(3)
# Output: [1, 2, 3]

# %%

target = []


def add_to_better(element, target=None):
    if target is None:
        target = []
    target.append(element)
    return target


add_to_better(1)
# Output: [1]

add_to_better(2)
# Output: [1, 2]

add_to_better(3)
# Output: [1, 2, 3]

# %%
