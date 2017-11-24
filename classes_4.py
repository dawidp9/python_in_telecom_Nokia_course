class Base(object):

    def __init__(self, var):
        self.__private = var

    def get_prvate(self):
        return self.__private


class Child(Base):

    def print_priv_var(self):
        print self._Base__private


Child("treasure").print_priv_var()