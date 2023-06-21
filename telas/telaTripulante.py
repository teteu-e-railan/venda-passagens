from telas.abstractTela import AbstractTela
import customtkinter

class TelaTripulante(AbstractTela):
    def __init__(self):
        super().__init__(
            {
                1: "Incluir Tripulante",
                2: "Alterar Tripulante",
                3: "Listar Tripulantes",
                4: "Excluir Tripulante",
                5: "Listar Registros",
                0: "Voltar",
            }
        )

    def mostra_opcoes(self) -> int:
        # Configurações da interface gráfica
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('green')

        # Criar uma nova janela
        nova_janela = customtkinter.CTk()
        nova_janela.geometry('500x600')
        nova_janela.title("Tela tripulante")

        opcao_selecionada = None

        def set_opcao_selecionada(index: int):
            nonlocal opcao_selecionada
            opcao_selecionada = index
            nova_janela.destroy()

        frame = customtkinter.CTkFrame(master=nova_janela, corner_radius=20, border_width=4, border_color='green')
        frame.pack(pady=20, padx=60, fill='both', expand=True)

        label = customtkinter.CTkLabel(master=frame, text="Tripulação", font=('Tahoma', 20))
        label.pack(pady=12, padx=10)

        for index, opcao in self.opcoes.items():
            button = customtkinter.CTkButton(master=frame, text=opcao, command=lambda index=index: set_opcao_selecionada(index))
            button.pack(pady=12, padx=10)

        nova_janela.mainloop()

        return opcao_selecionada

    def pega_dados_tripulante(self):
        print("-------- DADOS TRIPULANTES ----------")
        while True:
            nome = input("Nome: ").title().strip()
            if nome:
                break

            else:
                print("Dado invalido, digite novamente!!!")

        while True:
            cpf = input("CPF: ").strip()
            try:
                int(cpf)
                break

            except ValueError:
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
            try:
                telefone = int(telefone)
                break
            except ValueError:
                print("Dado invalido, digite novamente!!!")
        while True:
            cargo = input("Cargo: ").title().strip()
            if cargo:
                break

            else:
                print("Dado invalido, digite novamente!!!")

        return {
            "nome": nome,
            "cpf": cpf,
            "idade": idade,
            "telefone": telefone,
            "cargo": cargo,
        }

    # incluir def de alteração de dados*
    def altera_dados_tripulante(self):
        print("-------- DADOS Tripulante ----------")

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
            while True:
                cargo = input("Cargo: ").title().strip()
                if not cargo:
                    break

            return {
                "nome": nome,
                "cpf": cpf,
                "idade": idade,
                "telefone": telefone,
                "cargo": cargo,
            }

    def mostra_registro(self, dados_aviao: "dict[str, str | int]"):
        print("-------- LOG DE AÇÕES ----------")
        for index, valor in dados_aviao.items():
            print(f" {index} : {valor} ")

    def mostra_tripulante(self, dados_Tripulante: "dict[str, str | int]"):
        for index, valor in dados_Tripulante.items():
            print(f" {index} : {valor} ")

        print("\n")

    def seleciona_tripulante_por_cpf(self):
        cpf = input("CPF do tripulante que deseja selecionar: ").strip()
        return cpf
