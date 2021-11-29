from abc import ABCMeta


class Imposto(object):

    __metaclass__ = ABCMeta

    def calcular(self, orcamento, aliquota):
        imposto = 0
        try:
            imposto = orcamento.valor_total * 0.06
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