from telas.abstractTelaOpcoes import AbstractTelaOpcoes


class TelaSistema(AbstractTelaOpcoes):
    def __init__(self, parent, controller):
        super().__init__(
            parent,
            controller,
            opcoes={
                1: "Reservas",
                2: "Passageiros",
                3: "Tripulantes",
                4: "Voos",
                5: "Aviões",
                0: "Finalizar Sistema",
            },
        )
