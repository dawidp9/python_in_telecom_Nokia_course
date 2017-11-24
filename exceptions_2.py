class Pracownik(object):

    def __init__(self, imie, nazwisko):
        if (type(imie) != str) | (type(nazwisko) != str):
            raise Exception("cos jest nie tak!")

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


try:
    Manager("Jon", 5)
except Exception as details:
    print details
