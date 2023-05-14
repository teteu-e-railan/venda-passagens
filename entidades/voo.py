from datetime import date
from entidades.aviao import Aviao


class Voo:
    def __init__(
        self,
        partida: str,
        destino: str,
        data_do_voo: date,
        aviao: Aviao,
    ):
        self.__codigo = "1321"  # TODO autogenerate
        self.__partida = partida
        self.__destino = destino
        self.__data_do_voo = data_do_voo
        self.__aviao = aviao
        self.__assentos = []  # TODO gerar matriz de assentos

    @property
    def codigo(self) -> str:
        return self.__codigo

    @property
    def partida(self) -> str:
        return self.__partida

    @property
    def destino(self) -> str:
        return self.__destino

    @property
    def data_do_voo(self) -> date:
        return self.__data_do_voo

    @property
    def aviao(self):
        return self.__aviao

    @property
    def assentos(self):
        return self.__assentos

    @partida.setter
    def partida(self, partida: str):
        self.__partida = partida

    @destino.setter
    def destino(self, destino: str):
        self.__destino = destino

    @data_do_voo.setter
    def data_do_voo(self, data_do_voo: date):
        self.__data_do_voo = data_do_voo