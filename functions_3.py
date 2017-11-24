def fun(x, y):
    return filter(lambda n: (n % 2) != 0, map(lambda n: n*n, range(x, y+1)))

# better solution
def fun2(x, y):
    return [x*x for x in range(x, y+1) if (x % 2) != 0]


print fun(2, 5)
print fun2(2, 5)
