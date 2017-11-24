class Pracownik:

    def __init__(self, imie, nazwisko):
        if (type(imie) != str) | (type(nazwisko) != str):
            raise Exception("cos jest nie tak!")

        self.imie = imie
        self.nazwisko = nazwisko

    def __str__(self):
        return "{0}, {1}".format(self.imie, self.nazwisko)


print Pracownik("jan", 345)
