

class Orcamento(object):

    def __init__(self):
        self.__itens = []

    def obter_itens(self):
        return tuple(self.__)



class Item(object):

    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    @property
    def nome(self,nome):
        self.__nome = nome

    @property
    def valor(self):
        return self.__valor

    @property
    @valor.setter
    def valor(self, valor):
        self.__valor = valor







