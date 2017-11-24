class MulByN:

    def __init__(self, number):
        self.number = number

    def __mul__(self, other):
        return self.number * other


print MulByN(5) * 2