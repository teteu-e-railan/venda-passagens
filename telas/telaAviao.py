from telas.abstractTela import AbstractTela


class TelaAviao(AbstractTela):
    def __init__(self):
        super().__init__(
            {
                1: "Incluir Avião",
                2: "Alterar Avião",
                3: "Listar Aviões",
                4: "Excluir Avião",
                5: "Listar Registros",
                0: "Voltar",
            }
        )

    def tela_opcoes(self):
        print("-------- Aviões ----------")
        for index, opcao in self.opcoes.items():
            print(f"{index} - {opcao}")
        return self.verifica_opcao("Escolha uma opção: ")

    def pega_dados_aviao(self):
        print("-------- DADOS AVIÃO ----------")
        while True:
            modelo = input("Modelo: ").upper().strip()
            if modelo:
                break
            else:
                print("Dado invalido, digite novamente!!!")

        while True:
            fileiras = input("Fileiras: ").strip()
            if fileiras:
                try:
                    fileiras = int(fileiras)
                    break
                except ValueError:
                    print("Dado invalido, digite novamente!!!")
            else:
                print("Dado invalido, digite novamente!!!")
        while True:
            assentos_por_fileira = input("Assentos por fileira: ").strip()
            if assentos_por_fileira:
                try:
                    assentos_por_fileira = int(assentos_por_fileira)
                    break
                except ValueError:
                    print("Dado invalido, digite novamente!!!")
            else:
                print("Dado invalido, digite novamente!!!")

        return {
            "modelo": modelo,
            "fileiras": fileiras,
            "assentos_por_fileira": assentos_por_fileira,
        }

    def altera_dados_aviao(self):
        print("-------- DADOS PASSAGEIRO ----------")

        while True:
            modelo = input("modelo: ").upper().strip()

            while True:
                fileiras = input("fileiras: ").strip()

                if not fileiras:
                    break

                try:
                    fileiras = int(fileiras)
                    break
                except ValueError:
                    print("O fileiras deve ser composto apenas por números!")

            while True:
                assentos_por_fileira = input("assentos_por_fileira: ").strip()

                if not assentos_por_fileira:
                    break

                try:
                    assentos_por_fileira = int(assentos_por_fileira)
                    break
                except ValueError:
                    print("Assentos por fileira deve ser composta apenas por números!")

            return {
                "modelo": modelo,
                "fileiras": fileiras,
                "assentos_por_fileira": assentos_por_fileira,
            }

    def mostra_aviao(self, dados_aviao: "dict[str, str | int]"):
        for index, valor in dados_aviao.items():
            print(f" {index} : {valor} ")

    def mostra_registro(self, dados_aviao: "dict[str, str | int]"):
        print("-------- LOG DE AÇÕES ----------")
        for index, valor in dados_aviao.items():
            print(f" {index} : {valor} ")

    def mostra_modelo(self, avioes: list):
        print("Aviões disponíveis: ")
        for aviao in avioes:
            print(aviao.modelo)
        print("\n")

    def seleciona_aviao(self):
        modelo = input("Modelo do avião que deseja selecionar: ").upper().strip()
        return modelo
