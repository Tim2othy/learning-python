number_list = range(-5, 12)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)


is_odd = list(filter(lambda x: x % 2 != 0, number_list))
print(is_odd)
