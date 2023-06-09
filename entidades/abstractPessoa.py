from abc import ABC, abstractmethod


class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome: str, cpf: str, idade: int, telefone: int):
        self.__cpf = cpf
        self.__nome = nome
        self.__idade = idade
        self.__telefone = telefone

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str):
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: int):
        self.__telefone = telefone

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade: int):
        self.__idade = idade
