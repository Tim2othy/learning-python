def add(value1, value2):
    global result
    result = value1 + value2


add(2, 4)
print(result)

# don't use global variables


# %%


def profile():
    name = "Danny"
    age = 30
    return (name, age)


profile_data = profile()
print(profile_data[0])

print(profile_data[1])
