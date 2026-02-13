A = [1, 3, 2, 1, 2, 1, 5, 3, 3, 4, 2]
A = [1, 3, 2, 1, 2, 1, 7, 3, 3, 4, 2, 6]
A = [1, 7, 5, 6, 9, 1, 8]
A = [1, 7, 5, 6, 1, 3]


def solution(A):

    highest = 0
    largest_diff = 0
    current_hight = 0
    safe = 0

    h_of_max_diff = 0
    max_diff_after_peak = False

    for i in range(len(A)):
        previous_hight = current_hight
        current_hight = A[i]

        if previous_hight > current_hight:  # we're going down
            current_diff = highest - current_hight

            # Update largest diff so far
            if current_diff >= largest_diff:
                largest_diff = current_diff
                h_of_max_diff = current_hight
                max_diff_after_peak = True

        elif current_hight > previous_hight:  # we're going up

            # Update highest hight so far
            if current_hight > highest:
                highest = current_hight
                max_diff_after_peak = False
                safe = max(largest_diff, safe)
                continue
            else:
                if max_diff_after_peak:

                    could_be_safe = current_hight - h_of_max_diff

                    safe = max(could_be_safe, safe)

        else:
            continue

    return safe


print(solution(A))


# Get tallest value
# remember maximum of how much lower we are
# e.g. - 4, -8, -9...
# only exception is if we are last tallest value
# now say our best depth so far is -9
# we only remember values deeper than than that
# for each one we remember how high the mountain must
# eventually go to beat our best so far
# if the mountain ever goes this high it just becomes our new best
# if it doesn't it can be replaced by a different memory if
# a hole gets deeper, then anything that helps the
# previous hole also helps this one
