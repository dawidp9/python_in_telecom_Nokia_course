def sum_int(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

print sum_int(1, 2, 3, 4, 8)
