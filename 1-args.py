# *args


def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)


test_var_args("yasoob", "python", "eggs", "test")

# **kwargs


def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))


greet_me(name="timothy")


def keyword(entry):
    print("keyword argument:", entry)


keyword(entry="test")


def keyu(word):
    print("this is a test", word)


keyu(word="number one")

# This makes sense. It allowes you to pass variables with a name to a function.


def test_kwargs(**kwargs):
    for key, value in kwargs.items():
        if len(key) % 2 == 0:
            print(value)


test_kwargs(tt="two", ttt="three", tttt="four", ttttt="five")
