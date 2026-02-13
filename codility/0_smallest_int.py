A = [1, 3, 446, -44, -88, -9, 4864, -1, 2, 3, 6, 1, 55, -44564, 4]


def solution(A):

    a_sorted = sorted(A)
    a_pos = []

    k = 0
    for i in a_sorted:
        if i > 0 and k != i:
            a_pos.append(i)
        k = i

    x = 1
    for i in a_pos:
        if i == x:
            x += 1
            continue
        return x
    return x


s = solution(A)
print(s)


"""
so A has e.g. 50 items so we know 
the smallest int is smaller than 52
"""
