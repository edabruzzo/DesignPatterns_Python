from abc import ABCMeta


class Imposto(object):

    __metaclass__ = ABCMeta

    def calcular(self, orcamento, aliquota):
        imposto = 0
        try:
            imposto = orcamento.valor_total * aliquota
        except Exception as erro:
            print(erro)
            return 0
        return imposto


class ISS(Imposto):

    def   calcula(self, orcamento):
        return Imposto.calcular(self,  orcamento=orcamento, aliquota=0.1)


class ICMS(Imposto):

    def calcula(self, orcamento):
        return Imposto.calcular(self, orcamento=orcamento, aliquota=0.06)


class ICPP(Imposto):

    def calcula(self, orcamento):
        if orcamento.valor_total > 500:
            return Imposto.calcular(self, orcamento=orcamento, aliquota=0.07)
        else:
            return Imposto.calcular(self, orcamento=orcamento, aliquota=0.05)


class ICPP(Imposto):

    def calcula(self, orcamento):
        if orcamento.valor_total > 500 and self.__orcamento_possui_mais_de_um_item(orcamento):
            return Imposto.calcular(self, orcamento=orcamento, aliquota=0.1)
        else:
            return Imposto.calcular(self, orcamento=orcamento, aliquota=0.08)


    def __orcamento_possui_item_maior_cem_reais(self, orcamento):
        for item in orcamento.itens:
            if item.valor > 100:
                return True
        return False
