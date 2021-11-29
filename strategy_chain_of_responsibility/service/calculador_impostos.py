from strategy_chain_of_responsibility.model.orcamento import Orcamento, Item
from strategy_chain_of_responsibility.service.impostos import ISS, ICMS

class CalculadorImpostos(object):

    def realiza_calculo(self, orcamento, imposto):
        imposto_calculado = imposto.calcula(orcamento)
        print(f'Imposto {imposto_calculado}')
        return imposto_calculado



if __name__ == '__main__':

    calculador = CalculadorImpostos()

    orcamento1 = Orcamento()
    calculador.realiza_calculo(orcamento1, ISS())
    calculador.realiza_calculo(orcamento1, ICMS())

    # -------------------------------------------------
    orcamento2 = Orcamento()
    item1 = Item('Monitor Samsung',500)
    orcamento2.add_item(item1)
    calculador.realiza_calculo(orcamento2, ISS())
    calculador.realiza_calculo(orcamento2, ICMS())
