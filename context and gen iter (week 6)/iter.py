class Licznik():
    def __init__(self, min, max):
        self.min = min
        self.max = max+1
        self.current = self.min

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration()


iter = Licznik(3, 5)
print iter.__next__()
print iter.__next__()
print iter.__next__()

print "-----------------"


def gen_licznik(min, max):
    num = min
    while True:
        if num <= max:
            yield num
        num += 1


generator = gen_licznik(3, 5)
print next(generator)
print next(generator)
print next(generator)

print "-----------------"


def gen_fib(size):
    counter = 0
    fn1 = 0
    fn2 = 1
    while True:
        if counter < size:
            fn = fn1 + fn2
            yield fn
        fn2 = fn1
        fn1 = fn


gen_f = gen_fib(10)
print next(gen_f)
print next(gen_f)
print next(gen_f)
print next(gen_f)
print next(gen_f)
print next(gen_f)
print next(gen_f)
print next(gen_f)
