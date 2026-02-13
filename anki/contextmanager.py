from contextlib import contextmanager

# Remember a contextmanager generator must yield exactly once.


@contextmanager
def demo():
    print("A")
    yield 5456
    print("B")


with demo() as x:
    print("C")
    print(x)

# The with block automatically runs until yield, then does all the stuff in the with block
# Then runs everything after yield
