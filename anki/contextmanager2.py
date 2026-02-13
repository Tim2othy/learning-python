from contextlib import contextmanager

# this is the better way to use conext managers, including finally is safer


@contextmanager
def func():
    print("set up")
    try:
        yield "foo"
    finally:
        print("tear down")


with func():
    print("test")
