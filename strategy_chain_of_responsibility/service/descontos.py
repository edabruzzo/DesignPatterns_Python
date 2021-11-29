class Desconto(object):

    def __init__(self, proximo_desconto_cadeia=None):
        self.__proximo_desconto_cadeia = proximo_desconto_cadeia

    @property
    def proximo_desconto_cadeia(self):
        return self.__proximo_desconto_cadeia


    def calcular(self, orcamento, percentual, condicao):
        desconto = 0.0
        if condicao == True:
            desconto =  orcamento.valor_total * percentual
        else:
            if self.proximo_desconto_cadeia is not None:
                desconto = self.proximo_desconto_cadeia.calcula_desconto(orcamento)
        return desconto


class DescontoMaisCincoItens(Desconto):

    def __init__(self):
        super().__init__(DescontoValorMaiorQuinhentos())

    def calcula_desconto(self, orcamento):
        condicao = orcamento.total_itens > 5
        return Desconto.calcular(self, orcamento=orcamento, percentual=0.1,condicao=condicao)

class DescontoValorMaiorQuinhentos(Desconto):

    def __init__(self):
        Desconto.proximo_desconto_cadeia = SemDesconto()

    def calcula_desconto(self, orcamento):
        condicao = orcamento.valor_total > 500
        return Desconto.calcular(self, orcamento=orcamento, percentual=0.15,condicao=condicao)


class SemDesconto(object):

    def calcula_desconto(self, orcamento):
        return 0

