S = "44494"

"""
it has to contain only alphanumerical characters (a−z, A−Z, 0−9);
there should be an even number of letters;
there should be an odd number of digits.
"""


def solution(S):

    numbers = set()
    for n in range(10):
        numbers.add(str(n))

    def even_digits(strg: str):
        counter = 0
        for i in strg:
            if i in numbers:
                counter += 1

        is_even = counter % 2 == 0
        return is_even

    lst = S.split()

    word_length = -1

    for i in range(len(lst)):
        word = lst[i]

        if not word.isalnum():
            continue

        is_even = len(word) % 2 == 0
        if is_even:
            continue

        if even_digits(word):
            continue

        if len(word) > word_length:
            word_length = len(word)

    return word_length


print(solution(S))
