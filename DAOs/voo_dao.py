from DAOs.dao import DAO
from entidades.voo import Voo


class VooDAO(DAO):
    def __init__(self):
        super().__init__("voos.pkl")

    def add(self, voo: Voo):
        if (voo is not None) and isinstance(voo, Voo) and isinstance(voo.codigo, str):
            super().add(voo.codigo, voo)

    def update(self, voo: Voo):
        if (voo is not None) and isinstance(voo, Voo) and isinstance(voo.codigo, str):
            super().update(voo.codigo, voo)

    def get(self, key: str) -> Voo | None:
        if isinstance(key, str):
            return super().get(key)

    def get_all(self) -> list[Voo]:
        return super().get_all()

    def remove(selfself, key: str):
        if isinstance(key, str):
            return super().remove(key)
