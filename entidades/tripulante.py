from entidades.abstractPessoa import Pessoa


class Tripulante(Pessoa):
    def __init__(self, nome: str, cpf: str, idade: int, telefone: int, cargo: str):
        super().__init__(nome, cpf, idade, telefone)
        self.__cargo = cargo

    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo: str):
        self.__cargo = cargo
