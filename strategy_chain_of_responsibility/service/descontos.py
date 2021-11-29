class Desconto(object):

    def calcular(self, orcamento, percentual, condicao):
        if condicao == True:
            return orcamento.valor_total * percentual
        else:
            return 0


class DescontoMaisCincoItens(Desconto):

    def calcula_desconto(self, orcamento):
        condicao = orcamento.total_itens > 5
        return Desconto.calcular(self, orcamento=orcamento, percentual=0.1,condicao=condicao)

class DescontoValorMaiorQuinhentos(object):

    def calcula_desconto(self, orcamento):
        condicao = orcamento.valor_total > 500
        return Desconto.calcular(self, orcamento=orcamento, percentual=0.1,condicao=condicao)

