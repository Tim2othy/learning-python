from contextlib import contextmanager

# If a generator-based context manager acquires a resource before yield, put cleanup in finally.


@contextmanager
def demo():
    print("setup")
    try:
        yield
    finally:
        print("cleanup")


with demo():
    raise ValueError()

# even if an error happens the cleanup gets done anyway : )


"""
try:
    do stuff
finally:
    always cleanup
"""
