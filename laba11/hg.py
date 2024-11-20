def my_sum(a_list: list) -> int:
    if not a_list:
        return 0
    if len(a_list) == 1:
        return a_list[0]
    return a_list[0] + my_sum(a_list[1:])

m = my_sum([4])
print(m)