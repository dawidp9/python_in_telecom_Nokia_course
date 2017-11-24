class Pracownik(object):

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def __str__(self):
        return "{0}, {1}".format(self.imie, self.nazwisko)


class Programista(Pracownik):

    def __str__(self):
        return super(Programista, self).__str__() + " (programista)"


class Manager(Pracownik):

    def __str__(self):
        return super(Manager, self).__str__() + " (manager)"


print Programista("Jan", "Kowalski")
print Manager("Andrzej", "Duda")
