class NameTypeErr(Exception): pass
class SurnameTypeErr(Exception): pass


class Pracownik:

    def __init__(self, imie, nazwisko):
        try:
            if type(imie) != str:
                raise NameTypeErr("Name mast be string!")
        except NameTypeErr as err:
            print err
        try:
            if type(nazwisko) != str:
                raise SurnameTypeErr("Surname mast be string!")
        except SurnameTypeErr as err:
            print err

        self.imie = imie
        self.nazwisko = nazwisko

    def __str__(self):
        return "{0}, {1}".format(self.imie, self.nazwisko)


print Pracownik(1, 2)
