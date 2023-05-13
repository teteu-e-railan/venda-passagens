from telas.abstractTela import AbstractTela


class TelaReservas(AbstractTela):
    def __init__(self):
        super().__init__(
            {
                1: "Incluir Reserva",
                2: "Alterar Reserva",
                3: "Excluir Reserva",
                4: "Listar Reservas",
                0: "Retornar",
            }
        )

    def mostra_opcoes(self):
        print("-------- Sistema ----------")

        for index, opcao in self.opcoes.items():
            print(f"{index} - {opcao}")

        return self.verifica_opcao("Escolha uma opção: ")

    def mostra_reserva(self, dados_reserva: "dict[int, str]"):
        pass
