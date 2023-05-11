from telas.abstractTela import AbstractTela


class TelaSistema(AbstractTela):
    def __init__(self):
        super().__init__(
            {
                1: "Reservas",
                2: "Passageiros",
                3: "Tripulantes",
                4: "Voos",
                5: "Aviões",
                0: "Finalizar Sistema",
            }
        )

    def mostra_opcoes(self) -> int:
        print("-------- Sistema ----------")
        print("Escolha uma opção:")

        for index, opcao in self.opcoes.items():
            print(f"{index} - {opcao}")

        return self.verifica_opcao("Digite a opção: ")
