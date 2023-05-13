from telas.abstractTela import AbstractTela


class TelaAviao(AbstractTela):
    def __init__(self):
        super().__init__(
            {
                1: "Incluir Avião",
                2: "Alterar Avião",
                3: "Listar Aviões",
                4: "Excluir Avião",
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
            modelo = input("Modelo: ").upper()
            if modelo:
                break
            else:
                print("Dado invalido, digite novamente!!!")

        while True:
            fileiras = input("Fileiras: ")
            if fileiras:
                try:
                    fileiras = int(fileiras)
                    break
                except ValueError:
                    print("Dado invalido, digite novamente!!!")
            else:
                print("Dado invalido, digite novamente!!!")
        while True:
            assentos_por_fileira = input("Assentos por fileira: ")
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

    def mostra_aviao(self, dados_aviao):
        print("Modelo do Avião: ", dados_aviao["modelo"])
        print("fileiras: ", dados_aviao["fileiras"])
        print("assentos por fileira: ", dados_aviao["assentos_por_fileira"])
        print("\n")

    def seleciona_aviao(self):
        modelo = input("Modelo do avião que deseja selecionar: ").upper()
        return modelo
