from DAOs.dao import DAO
from entidades.reserva import Reserva


class ReservaDAO(DAO):
    def __init__(self):
        super().__init__("reservas.pkl")

    def add(self, reserva: Reserva):
        if (
            (reserva is not None)
            and isinstance(reserva, Reserva)
            and isinstance(reserva.codigo, str)
        ):
            super().add(reserva.codigo, reserva)

    def update(self, reserva: Reserva):
        if (
            (reserva is not None)
            and isinstance(reserva, Reserva)
            and isinstance(reserva.codigo, str)
        ):
            super().update(reserva.codigo, reserva)

    def get(self, key: str) -> "Reserva | None":
        if isinstance(key, str):
            return super().get(key)

    def get_all(self) -> "list[Reserva]":
        return list(super().get_all())

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
