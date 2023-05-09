from abstractPessoa import Pessoa

class Tripulante(Pessoa):
    def __init__(self, cpf: int, nome: str, telefone: int, idade: int, cargo: str):
        super().__init__(cpf, nome, telefone, idade)
        self.__cargo = cargo

    @property
    def cargo(self):
        return self.__cargo
    @cargo.setter
    def cargo(self, cargo: str):
        self.__cargo = cargo
