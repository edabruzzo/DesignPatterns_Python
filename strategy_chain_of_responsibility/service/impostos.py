from abc import ABCMeta, abstractmethod


class Imposto(object):

    __metaclass__ = ABCMeta

    def calcula(self, orcamento):
        imposto = 0
        try:
            if self.deve_usar_maxima_taxacao(orcamento):
               imposto = self.maxima_taxacao(orcamento)
            else:
                imposto = self.minima_taxacao(orcamento)
        except Exception as erro:
            print(erro)
            return 0
        return imposto


    @abstractmethod
    def deve_usar_maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def minima_taxacao(self, orcamento):
        pass


class ISS(Imposto):

    def deve_usar_maxima_taxacao(self, orcamento):
        return True

    def maxima_taxacao(self, orcamento):
        return orcamento.valor_total * 0.1

    def minima_taxacao(self, orcamento):
        return 0


class ICMS(Imposto):

    def deve_usar_maxima_taxacao(self, orcamento):
        return True

    def maxima_taxacao(self, orcamento):
        return orcamento.valor_total * 0.06

    def minima_taxacao(self, orcamento):
        return 0



class ICPP(Imposto):

    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor_total > 500

    def maxima_taxacao(self, orcamento):
        return orcamento.valor_total * 0.07

    def minima_taxacao(self, orcamento):
        return orcamento.valor_total * 0.05



class IKCV(Imposto):

    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor_total > 500 and self.__orcamento_possui_mais_de_um_item(orcamento)

    def maxima_taxacao(self, orcamento):
        return orcamento.valor_total * 0.1

    def minima_taxacao(self, orcamento):
        return orcamento.valor_total * 0.08


    def __orcamento_possui_item_maior_cem_reais(self, orcamento):
        for item in orcamento.itens:
            if item.valor > 100:
                return True
        return False