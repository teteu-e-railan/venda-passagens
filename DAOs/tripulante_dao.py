from DAOs.dao import DAO
from entidades.tripulante import Tripulante


class TripulanteDAO(DAO):
    def __init__(self):
        super().__init__("tripulantes.pkl")

    def add(self, tripulante: Tripulante):
        if (
            (tripulante is not None)
            and isinstance(tripulante, Tripulante)
            and isinstance(tripulante.cpf, str)
        ):
            super().add(tripulante.cpf, tripulante)

    def update(self, tripulante: Tripulante):
        if (
            (tripulante is not None)
            and isinstance(tripulante, Tripulante)
            and isinstance(tripulante.cpf, str)
        ):
            super().update(tripulante.cpf, tripulante)

    def get(self, key: str) -> "Tripulante | None":
        if isinstance(key, str):
            return super().get(key)

    def get_all(self) -> "list[Tripulante]":
        return list(super().get_all())

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
