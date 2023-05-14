from entidades.abstractPessoa import Pessoa


class Passageiro(Pessoa):
    def __init__(self, cpf: int, nome: str, telefone: int, idade: int):
        super().__init__(cpf, nome, telefone, idade)
