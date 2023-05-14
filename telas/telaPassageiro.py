from telas.abstractTela import AbstractTela


class TelaPassagerio(AbstractTela):
    def __init__(self):
        super().__init__(
            {
                1: "Incluir Passageiro",
                2: "Alterar Passageiro",
                3: "Listar Passageiros",
                4: "Excluir Passageiro",
                0: "Voltar",
            }
        )

    def tela_opcoes(self):
        print("-------- Passageiro ----------")
        for index, opcao in self.opcoes.items():
            print(f"{index} - {opcao}")
        return self.verifica_opcao("Escolha uma opção: ")

    def pega_dados_passageiro(self):
        print("-------- DADOS PASSAGEIRO ----------")
        while True:
            nome = input("Nome: ").upper().strip()
            if nome:
                break

            else:
                print("Dado invalido, digite novamente!!!")

        while True:
            cpf = input("CPF: ").strip()
            if cpf:
                try:
                    cpf = int(cpf)
                    break

                except ValueError:
                    print("Dado invalido, digite novamente!!!")
            else:
                print("Dado invalido, digite novamente!!!")
        while True:
            idade = input("Idade: ").strip()
            if idade:
                try:
                    idade = int(idade)
                    break

                except ValueError:
                    print("Dado invalido, digite novamente!!!")
            else:
                print("Dado invalido, digite novamente!!!")
        while True:
            telefone = input("Telefone: ").strip()
            if telefone:
                try:
                    telefone = int(telefone)
                    break

                except ValueError:
                    print("Dado invalido, digite novamente!!!")
            else:
                print("Dado invalido, digite novamente!!!")

        return {
            "nome": nome,
            "cpf": cpf,
            "idade": idade,
            "telefone": telefone,
        }

    def mostra_passageiro(self, dados_passageiro):
        nome = dados_passageiro["nome"]
        cpf = dados_passageiro["cpf"]
        idade = dados_passageiro["idade"]
        telefone = dados_passageiro["telefone"]

        print(f"Nome do Passageiro: {nome}")
        print(f"Documento: {cpf}.")
        print(f"Idade: {idade}.")
        print(f"Telefone: {telefone}.")

    def mostra_nome(self, passageiros: list):
        print("Passageiros Cadastrados: ")
        for passageiro in passageiros:
            print(passageiro.nome)
        print("\n")

    def seleciona_passageiro(self):
        nome = input("nome do passageiro que deseja selecionar: ").upper().strip()
        return nome

    def confirma_opcao(self, mensagem: str) -> bool:
        while True:
            try:
                opcao = input(mensagem + " (S/N) ").upper().strip()
                if opcao not in ["S", "N"]:
                    raise Exception
                return opcao == "S"
            except Exception:
                print("Opção inválida!")
