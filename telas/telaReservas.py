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
        print("-------- Reservas ----------")

        for index, opcao in self.opcoes.items():
            print(f"{index} - {opcao}")

        return self.verifica_opcao("Escolha uma opção: ")

    def pega_dados_reserva(self):
        assento = input("Digite o assento desejado: ")
        # TODO verificar se assento está disponível

        cpf_passageiro = input("Digite o CPF do passageiro: ")
        # TODO verificar se CPF existe

        codigo_voo = input("Digite o código do Voo: ")
        # TODO verificar se voo existe

        return {
            "assento": assento,
            "cpf_passageiro": cpf_passageiro,
            "codigo_voo": codigo_voo,
        }

    def mostra_reserva(self, dados_reserva: "dict[str, str]"):
        if dados_reserva is None:
            print("Não há nenhuma reserva registrada ainda :( ")

        else:
            for chave, valor in dados_reserva.items():
                print(f"{chave}: {valor}")

    def seleciona_reserva(self) -> str:
        codigo_reserva = input("Insira o código da reserva que deseja buscar: ")

        return codigo_reserva
