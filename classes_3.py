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


class Firma():

    def __init__(self, pracownicy):
        self.pracownicy = pracownicy

    def __str__(self):
        p_str = "Pracownicy: \n"
        for pracownik in self.pracownicy:
            p_str += (str(pracownik)+"\n")
        return p_str


pracownicy = [Programista("Guido", "van Rossum"),
              Programista("Rowan", "Mr.Bean"),
              Manager("Steve", "Jobs")]

print Firma(pracownicy)