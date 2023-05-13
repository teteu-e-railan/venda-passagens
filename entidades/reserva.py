class Reserva:
    def __init__(self, assento, passageiro, voo) -> None:
        # gerar randomicamente
        self.__codigo = 2
        self.__assento = assento
        self.__passageiro = passageiro
        self.__voo = voo

    @property
    def codigo(self):
        return self.__codigo

    @property
    def assento(self):
        return self.__assento
