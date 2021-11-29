from strategy_chain_of_responsibility.model.orcamento import Orcamento
from strategy_chain_of_responsibility.service.impostos import ISS, ICMS

class CalculadorImpostos(object):

    def realiza_calculo(self, orcamento, imposto):
        imposto_calculado = imposto.calcula(orcamento)
        print(f'Imposto {imposto_calculado}')
        return imposto_calculado



if __name__ == '__main__':
    calculador = CalculadorImpostos()
    orcamento = Orcamento(10000)
    calculador.realiza_calculo(orcamento, ISS())
    calculador.realiza_calculo(orcamento, ICMS())
