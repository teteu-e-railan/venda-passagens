from DAOs.dao import DAO
from entidades.aviao import Aviao


class AviaoDAO(DAO):
    def __init__(self):
        super().__init__("avioes.pkl")

    def add(self, aviao: Aviao):
        if (
            (aviao is not None)
            and isinstance(aviao, Aviao)
            and isinstance(aviao.modelo, str)
        ):
            super().add(aviao.modelo, aviao)

    def update(self, aviao: Aviao):
        if (
            (aviao is not None)
            and isinstance(aviao, Aviao)
            and isinstance(aviao.modelo, str)
        ):
            super().update(aviao.modelo, aviao)

    def get(self, key: str) -> "Aviao | None":
        if isinstance(key, str):
            return super().get(key)

    def get_all(self) -> "list[Aviao]":
        return list(super().get_all())

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
