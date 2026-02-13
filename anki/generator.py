# Generator function


def g():
    print("first")
    yield 1
    print("second")
    yield 2
    print("third")
    yield 3


gen = g()

print(next(gen))
next(gen)
print(next(gen))

# If we run it again it produces an error

# print(next(gen))


# But we can restart the function and then it works again
print("Next try")
gen = g()
print(next(gen))

print(next(g()))
print(next(g()))
print(next(g()))
print(next(g()))
print(next(gen))

# Ok und just calling the function directly just runs until the first yield
