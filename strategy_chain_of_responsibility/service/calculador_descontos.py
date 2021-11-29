#!/usr/bin/python
# -*- coding: <encoding name> -*-

'''
Convenção no Python para dizer ao interpretador que o encoding do arquivo
é UTF-8, do contrário o default é ASCII

https://www.python.org/dev/peps/pep-0263/
https://github.com/python
https://github.com/python/peps
'''
from strategy_chain_of_responsibility.service.descontos import DescontoValorMaiorQuinhentos


class CalculadorDescontos(object):

    def calcula_desconto(self, orcamento, desconto):
        return desconto.calcula_desconto(orcamento)


if __name__ == '__main__':

    from strategy_chain_of_responsibility.model.orcamento import Orcamento, Item

    item1 = Item('Monitor Samsung', 500)
    item2 = Item(valor=300, nome='Monitor Positivo')
    item3 = Item('Monitor Semp Toshiba', 400)

    orcamento1 = Orcamento()
    orcamento1.add_item(item1)

    orcamento2 = Orcamento()
    orcamento2.add_item(item2)
    orcamento2.add_item(item3)

    print(str(orcamento1.valor_total))
    print(str(orcamento2.valor_total))

    valor_desconto = CalculadorDescontos().calcula_desconto(orcamento1, DescontoValorMaiorQuinhentos())
    print(valor_desconto)

    valor_desconto = CalculadorDescontos().calcula_desconto(orcamento2, DescontoValorMaiorQuinhentos())
    print(valor_desconto)