

class Orcamento(object):

    def __init__(self):
        self.__itens = []


    @property
    def itens(self):
        return self.__itens

    @itens.setter
    @property
    def itens(self, itens):
        self.__itens = itens

    @property
    def valor(self):
        total = 0.0
        for item in self.__itens:
            total += item.valor()
        return total


    def obter_itens(self):
        return tuple(self.__)

    @property
    def total_itens(self):
        return len(self.__itens)


    def add_item(self, item):
        self.__itens.append(item)


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







