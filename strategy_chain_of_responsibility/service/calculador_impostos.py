from strategy_chain_of_responsibility.model.orcamento import Orcamento, Item
from strategy_chain_of_responsibility.service.impostos import ISS,ICMS,ICPP, IKCV

class CalculadorImpostos(object):

    def realiza_calculo(self, orcamento, imposto):
        imposto_calculado = imposto.calcula(orcamento)
        print(f'Imposto {imposto_calculado}')
        return imposto_calculado



if __name__ == '__main__':

    calculador = CalculadorImpostos()
    lista_impostos = [ISS(),ICMS(), ICPP(), IKCV()]

    orcamento1 = Orcamento()
    for imposto in lista_impostos:
        calculador.realiza_calculo(orcamento1, imposto)

    # -------------------------------------------------
    orcamento2 = Orcamento()
    item1 = Item('Monitor Samsung',500)
    orcamento2.add_item(item1)

    for imposto in lista_impostos:
        calculador.realiza_calculo(orcamento2, imposto)
