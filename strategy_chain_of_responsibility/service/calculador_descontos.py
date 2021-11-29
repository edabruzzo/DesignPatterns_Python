#!/usr/bin/python
# -*- coding: <encoding name> -*-

'''
Convenção no Python para dizer ao interpretador que o encoding do arquivo
é UTF-8, do contrário o default é ASCII

https://www.python.org/dev/peps/pep-0263/
https://github.com/python
https://github.com/python/peps
'''


class CalculadorDescontos(object):

    def calcula_desconto(self, orcamento):
        if orcamento.total_itens > 5:
            return orcamento.valor * 0.1
        elif orcamento.valor > 500:
            return orcamento.valor * 0.07


if __name__ == '__main__':

    from strategy_chain_of_responsibility.model.orcamento import Orcamento, Item

    item1 = Item(500, 'Monitor Positivo')
    item2 = Item(400, 'Monitor Samsung')
    item3 = Item(20, 'Mouse Multilaser')

    orcamento1 = Orcamento()
    orcamento1.add_item(item1)

    orcamento2 = Orcamento()
    orcamento2.add_item(item2)
    orcamento2.add_item(item3)

    print(orcamento1.valor)
    print(orcamento2.valor)
