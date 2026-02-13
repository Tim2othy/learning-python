nums = [i for i in range(1_000_000)]
nums = (i for i in range(1_000_000))

# This:
# doesn’t store all numbers
# generates them when needed
# saves memory


def read_lines(file):
    for line in file:
        print(line)
        yield line


file = range(1_000)

gen = read_lines(file)
next(gen)
next(gen)
next(gen)
next(gen)

# A generator:
# Runs until yield → pauses → resumes on next().
