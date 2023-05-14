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
            nome = input("Nome: ").title().strip()
            if nome:
                break

            else:
                print("Dado invalido, digite novamente!!!")

        while True:
            cpf = input("CPF: ").strip()
            if cpf:
                break

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
                break

            else:
                print("Dado invalido, digite novamente!!!")

        return {
            "nome": nome,
            "cpf": cpf,
            "idade": idade,
            "telefone": telefone,
        }

    # incluir def de alteração de dados*
    def altera_dados_passageiro(self):
        print("-------- DADOS PASSAGEIRO ----------")

        while True:
            nome = input("Nome: ").title().strip()

            while True:
                cpf = input("CPF: ").strip()

                if not cpf:
                    break

                try:
                    int(cpf)
                    break
                except ValueError:
                    print("O CPF deve ser composto apenas por números!")

            while True:
                idade = input("Idade: ").strip()

                if not idade:
                    break

                try:
                    idade = int(idade)
                    break
                except ValueError:
                    print("A idade deve ser composta apenas por números!")

            while True:
                telefone = input("Telefone: ").strip()

                if not telefone:
                    break

                try:
                    telefone = int(telefone)
                    break
                except ValueError:
                    print("O Telefone deve ser composto apenas por números!")

            return {
                "nome": nome,
                "cpf": cpf,
                "idade": idade,
                "telefone": telefone,
            }

    def mostra_passageiro(self, dados_passageiro: "dict[str, str | int]"):
        for index, valor in dados_passageiro.items():
            print(f" {index} : {valor} ")

        print("\n")

    def seleciona_passageiro_por_cpf(self):
        cpf = input("CPF do passageiro que deseja selecionar: ").strip()
        return cpf

    def confirma_opcao(self, mensagem: str) -> bool:
        while True:
            try:
                opcao = input(mensagem + " (S/N) ").upper().strip()
                if opcao not in ["S", "N"]:
                    raise Exception
                return opcao == "S"
            except Exception:
                print("Opção inválida!")
