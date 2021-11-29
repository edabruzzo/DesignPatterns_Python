class Imposto(object):

    def calcula(self, orcamento, aliquota):
        imposto = 0
        try:
            imposto = orcamento.valor * 0.06
        except Exception as erro:
            print(erro)
            return 0
        return imposto


class ISS(Imposto):
    def calcula(self, orcamento):
        return Imposto.calcula(orcamento, 0.1)


class ICMS(Imposto):
    def calcula(self, orcamento):
        return Imposto.calcula(orcamento, 0.06)