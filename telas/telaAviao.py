from controladores.controladorAviao import ControladorAviao


class TelaAviao:
    def tela_opcoes(self):
        print("-------- Aviões ----------")
        print("Escolha a opcao")
        print("1 - Incluir Avião")
        print("2 - Alterar Avião")
        print("3 - Listar Aviões")
        print("4 - Excluir Avião")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_aviao(self):
        print("-------- DADOS AVIÃO ----------")
        modelo = input("Modelo: ")
        fileiras = input("Fileiras: ")
        assentos_por_fileira = input("Assentos por fileira: ")

        return {
            "modelo": modelo,
            "Fileiras": fileiras,
            "assentos_por_fileira": assentos_por_fileira,
        }

    def mostra_aviao(self, dados_aviao):
        print("Modelo do Avião: ", dados_aviao["modelo"])
        print("fileiras: ", dados_aviao["fileiras"])
        print("assentos por fileira: ", dados_aviao["assento_por_fileiras"])
        print("\n")

    def seleciona_aviao(self):
        modelo = input("Modelo do avião que deseja selecionar: ")
        return modelo

    def mostra_mensagem(self, msg):
        print(msg)
