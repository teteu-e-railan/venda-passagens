from DAOs.dao import DAO
from entidades.passageiro import Passageiro


class PassageiroDAO(DAO):
    def __init__(self):
        super().__init__("passageiros.pkl")

    def add(self, passageiro: Passageiro):
        if (
            (passageiro is not None)
            and isinstance(passageiro, Passageiro)
            and isinstance(passageiro.cpf, str)
        ):
            super().add(passageiro.cpf, passageiro)

    def update(self, passageiro: Passageiro):
        if (
            (passageiro is not None)
            and isinstance(passageiro, Passageiro)
            and isinstance(passageiro.cpf, str)
        ):
            super().update(passageiro.cpf, passageiro)

    def get(self, key: str) -> "Passageiro | None":
        if isinstance(key, str):
            return super().get(key)

    def get_all(self) -> "list[Passageiro]":
        return list(super().get_all())

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
