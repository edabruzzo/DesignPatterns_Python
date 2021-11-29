class Desconto(object):

    def __init__(self, proximo_desconto_cadeia):
        self.__proximo_desconto_cadeia = proximo_desconto_cadeia


    def calcular(self, orcamento, percentual, condicao):
        desconto = 0.0
        if condicao == True:
            desconto =  orcamento.valor_total * percentual
        else:
            if self.__proximo_desconto_cadeia is not None:
                desconto = self.__proximo_desconto_cadeia.calcula_desconto(orcamento)
        return desconto

class DescontoMaisCincoItens(Desconto):

    def __init__(self):
        Desconto.__init__(DescontoValorMaiorQuinhentos())

    def calcula_desconto(self, orcamento):
        condicao = orcamento.total_itens > 5
        return Desconto.calcular(self, orcamento=orcamento, percentual=0.1,condicao=condicao)

class DescontoValorMaiorQuinhentos(object):

    def calcula_desconto(self, orcamento):
        condicao = orcamento.valor_total > 500
        return Desconto.calcular(self, orcamento=orcamento, percentual=0.1,condicao=condicao)

