from helpers.gerador_id import gerar_id
from entidades.passageiro import Passageiro
from entidades.voo import Voo


class Reserva:
    # TODO tipar os parâmetros passageiro e voo
    def __init__(self, fileira: int, assento: int, passageiro: Passageiro, voo: Voo):
        self.__codigo = gerar_id()
        self.__fileira = fileira
        self.__assento = assento
        self.__passageiro = passageiro
        self.__voo = voo

    @property
    def codigo(self) -> str:
        return self.__codigo

    @property
    def fileira(self) -> int:
        return self.__fileira

    @property
    def assento(self) -> int:
        return self.__assento

    @property
    def passageiro(self) -> Passageiro:
        return self.__passageiro

    @property
    def voo(self) -> Voo:
        return self.__voo

    @fileira.setter
    def fileira(self, fileira: int):
        self.__fileira = fileira

    @assento.setter
    def assento(self, assento: int):
        self.__assento = assento

    @passageiro.setter
    def passageiro(self, passageiro):
        self.__passageiro = passageiro
