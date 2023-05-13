from helpers.gerador_id import gerador_id


class Reserva:
    # TODO tipar os parâmetros passageiro e voo
    def __init__(self, assento: str, passageiro, voo):
        self.__codigo = gerador_id()
        self.__assento = assento
        self.__passageiro = passageiro
        self.__voo = voo

    @property
    def codigo(self) -> str:
        return self.__codigo

    @property
    def assento(self) -> str:
        return self.__assento

    @property
    def passageiro(self):
        return self.__passageiro

    @property
    def voo(self):
        return self.__voo

    @assento.setter
    def assento(self, assento: str):
        self.__assento = assento

    @passageiro.setter
    def passageiro(self, passageiro):
        self.__passageiro = passageiro
