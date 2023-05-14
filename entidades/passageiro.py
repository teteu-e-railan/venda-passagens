from entidades.abstractPessoa import Pessoa


class Passageiro(Pessoa):
    def __init__(self, nome: str, cpf: str, idade: int, telefone: int):
        super().__init__(nome, cpf, idade, telefone)
