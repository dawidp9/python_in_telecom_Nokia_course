def fib(n):
    fib_n = 0
    fib_n_1 = 1
    l = [0, 1]

    for i in range(n-1):
        fib = fib_n + fib_n_1
        l.append(fib)
        fib_n = fib_n_1
        fib_n_1 = fib

    return l

print fib(14)