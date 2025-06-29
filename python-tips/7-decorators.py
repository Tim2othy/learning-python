def hi(name="tim"):
    return "hi " + name


print(hi("5"))

greet = hi

del hi

# now hi() will raise an error

print(greet("t"))
