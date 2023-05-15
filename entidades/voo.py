from datetime import date
from entidades.aviao import Aviao
from helpers.gerador_id import gerar_id
from helpers.gerar_matriz_assentos import gerar_matriz_assentos


class Voo:
    def __init__(
        self,
        partida: str,
        destino: str,
        data_do_voo: str,
        aviao: Aviao,
    ):
        self.__codigo = gerar_id()
        self.__partida = partida
        self.__destino = destino
        self.__data_do_voo = date.fromisoformat(data_do_voo)
        self.__aviao = aviao
        self.__assentos = gerar_matriz_assentos(
            self.aviao.fileiras, self.aviao.assentos_por_fileira
        )

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
    def data_do_voo(self, data_do_voo: str):
        self.__data_do_voo = date.fromisoformat(data_do_voo)

    def reservar_assento(self, fileira: int, assento_fileira: int):
        self.assentos[fileira][assento_fileira] = "X"
