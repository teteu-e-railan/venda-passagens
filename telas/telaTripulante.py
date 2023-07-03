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
    
    # Configurações da interface gráfica
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('green')

    def mostra_opcoes(self) -> int:
        # Criar uma nova janela
        nova_janela = customtkinter.CTk()
        nova_janela.geometry(self.centralizar_janela(nova_janela, 500, 600))
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
        # Criar uma nova janela
        nova_janela = customtkinter.CTk()
        nova_janela.geometry(self.centralizar_janela(nova_janela, 500, 600))
        nova_janela.title("Dados do Tripulante")

        dados = {}

        def confirmar():
            nonlocal dados
            nome = nome_entry.get().strip()
            cpf = cpf_entry.get().strip()
            idade = idade_entry.get().strip()
            telefone = telefone_entry.get().strip()
            cargo = cargo_entry.get().strip()

            # Validar os dados
            if not nome:
                label_mensagem = customtkinter.CTkLabel(master=frame_principal, text="Nome inválido, digite novamente!", font=('Tahoma', 12))
                label_mensagem.pack(pady=10)
                label_mensagem.after(4000, lambda: label_mensagem.destroy())
                return

            try:
                int(cpf)
            except ValueError:
                label_mensagem = customtkinter.CTkLabel(master=frame_principal, text="CPF inválido, digite apenas números!", font=('Tahoma', 12))
                label_mensagem.pack(pady=10)
                label_mensagem.after(4000, lambda: label_mensagem.destroy())
                return

            try:
                int(idade)
            except ValueError:
                label_mensagem = customtkinter.CTkLabel(master=frame_principal, text="Idade inválida, digite apenas números!", font=('Tahoma', 12))
                label_mensagem.pack(pady=10)
                label_mensagem.after(4000, lambda: label_mensagem.destroy())
                return

            try:
                int(telefone)
            except ValueError:
                label_mensagem = customtkinter.CTkLabel(master=frame_principal, text="Telefone inválido, digite apenas números!", font=('Tahoma', 12))
                label_mensagem.pack(pady=10)
                label_mensagem.after(4000, lambda: label_mensagem.destroy())
                return

            # Armazenar os dados
            dados["nome"] = nome
            dados["cpf"] = cpf
            dados["idade"] = idade
            dados["telefone"] = telefone
            dados["cargo"] = cargo

            label_mensagem = customtkinter.CTkLabel(master=frame_principal, text="Dados inseridos com sucesso!", font=('Tahoma', 20))
            label_mensagem.pack(pady=50)
            nova_janela.update_idletasks()
            nova_janela.after(1000, nova_janela.destroy)

        frame_principal = customtkinter.CTkFrame(master=nova_janela, corner_radius=20, border_width=4, border_color='green')
        frame_principal.pack(pady=20, padx=60, fill='both', expand=True)

        label_titulo = customtkinter.CTkLabel(master=frame_principal, text="Dados do Tripulante", font=('Tahoma', 16))
        label_titulo.pack(pady=12, padx=10)

        nome_entry = customtkinter.CTkEntry(master=frame_principal, placeholder_text="Nome", width=200)
        nome_entry.pack(pady=5, padx=10)

        cpf_entry = customtkinter.CTkEntry(master=frame_principal, placeholder_text="CPF", width=200)
        cpf_entry.pack(pady=5, padx=10)

        idade_entry = customtkinter.CTkEntry(master=frame_principal, placeholder_text="Idade", width=200)
        idade_entry.pack(pady=5, padx=10)

        telefone_entry = customtkinter.CTkEntry(master=frame_principal, placeholder_text="Telefone", width=200)
        telefone_entry.pack(pady=5, padx=10)

        cargo_entry = customtkinter.CTkEntry(master=frame_principal, placeholder_text="Cargo", width=200)
        cargo_entry.pack(pady=5, padx=10)

        botao_confirmar = customtkinter.CTkButton(master=frame_principal, text="Confirmar", command=confirmar)
        botao_confirmar.pack(pady=10, padx=10)

        nova_janela.mainloop()

        return dados

    def altera_dados_tripulante(self):
        # Criar uma nova janela
        nova_janela = customtkinter.CTk()
        nova_janela.geometry(self.centralizar_janela(nova_janela, 500, 600))
        nova_janela.title("Alterar Dados do Tripulante")

        dados = {}

        def confirmar():
            nonlocal dados
            nome = entry_nome.get().strip()
            cpf = entry_cpf.get().strip()
            idade = entry_idade.get().strip()
            telefone = entry_telefone.get().strip()
            cargo = entry_cargo.get().strip()

            # Validar os dados
            if not nome:
                label_mensagem = customtkinter.CTkLabel(master=frame, text="Nome inválido, digite novamente!", font=('Tahoma', 12))
                label_mensagem.pack(pady=30)
                label_mensagem.after(4000, lambda: label_mensagem.destroy())
                return

            try:
                int(cpf)
            except ValueError:
                label_mensagem = customtkinter.CTkLabel(master=frame, text="CPF inválido, digite novamente!", font=('Tahoma', 12))
                label_mensagem.pack(pady=10)
                label_mensagem.after(4000, lambda: label_mensagem.destroy())
                return

            if not idade:
                label_mensagem = customtkinter.CTkLabel(master=frame, text="Idade inválida, digite novamente!", font=('Tahoma', 12))
                label_mensagem.pack(pady=10)
                label_mensagem.after(4000, lambda: label_mensagem.destroy())
                return

            try:
                int(idade)
            except ValueError:
                label_mensagem = customtkinter.CTkLabel(master=frame, text="Idade inválida, digite novamente!", font=('Tahoma', 12))
                label_mensagem.pack(pady=10)
                label_mensagem.after(4000, lambda: label_mensagem.destroy())
                return

            try:
                int(telefone)
            except ValueError:
                label_mensagem = customtkinter.CTkLabel(master=frame, text="Telefone inválido, digite novamente!", font=('Tahoma', 12))
                label_mensagem.pack(pady=10)
                label_mensagem.after(1000, lambda: label_mensagem.destroy())
                return

            # Armazenar os dados
            dados["nome"] = nome
            dados["cpf"] = cpf
            dados["idade"] = idade
            dados["telefone"] = telefone
            dados["cargo"] = cargo

            label_mensagem = customtkinter.CTkLabel(master=frame, text="Dados inseridos com sucesso!", font=('Tahoma', 20))
            label_mensagem.pack(pady=50)
            nova_janela.update_idletasks()
            nova_janela.after(1000, nova_janela.destroy())

        frame = customtkinter.CTkFrame(master=nova_janela, corner_radius=20, border_width=4, border_color='green')
        frame.pack(pady=20, padx=60, fill='both', expand=True)

        label = customtkinter.CTkLabel(master=frame, text="Alterar Dados do Tripulante", font=('Tahoma', 20))
        label.pack(pady=12, padx=10, fill='both', expand=True)

        entry_nome = customtkinter.CTkEntry(master=frame, placeholder_text="Digite o nome", width=200)
        entry_nome.pack(pady=5)

        entry_cpf = customtkinter.CTkEntry(master=frame, placeholder_text="Digite o CPF", width=200)
        entry_cpf.pack(pady=5)

        entry_idade = customtkinter.CTkEntry(master=frame, placeholder_text="Digite a idade", width=200)
        entry_idade.pack(pady=5)

        entry_telefone = customtkinter.CTkEntry(master=frame, placeholder_text="Digite o telefone", width=200)
        entry_telefone.pack(pady=5)

        entry_cargo = customtkinter.CTkEntry(master=frame, placeholder_text="Digite o cargo", width=200)
        entry_cargo.pack(pady=5)

        button_confirmar = customtkinter.CTkButton(master=frame, text="Confirmar", command=confirmar, width=10)
        button_confirmar.pack(pady=10)

        nova_janela.mainloop()

        return dados


    def mostra_registro(self, dados_aviao):
        nova_janela = customtkinter.CTk()
        nova_janela.geometry(self.centralizar_janela(nova_janela, 500, 600))
        nova_janela.title("Log de Ações")

        frame_principal = customtkinter.CTkFrame(master=nova_janela, corner_radius=20, border_width=4, border_color='green')
        frame_principal.pack(pady=20, padx=60)

        label_titulo = customtkinter.CTkLabel(master=frame_principal, text="Log de Ações", font=('Tahoma', 16))
        label_titulo.pack(pady=12)

        for chave, valor in dados_aviao.items():
            dados = f"{chave}: {valor}"
            label_dado = customtkinter.CTkLabel(master=frame_principal, text=dados)
            label_dado.pack()
        botao_voltar = customtkinter.CTkButton(master=frame_principal, text="OK", command=nova_janela.destroy)
        botao_voltar.pack(pady=10)
        nova_janela.mainloop()


    def mostra_tripulante(self, dados_tripulante):
        nova_janela = customtkinter.CTk()
        nova_janela.geometry(self.centralizar_janela(nova_janela, 500, 600))
        nova_janela.title("Dados do Tripulante")

        frame_principal = customtkinter.CTkFrame(master=nova_janela, corner_radius=20, border_width=4, border_color='green')
        frame_principal.pack(pady=20, padx=60, fill='both', expand=True)

        for chave, valor in dados_tripulante.items():
            dados = f"{chave}: {valor}"
            label_dados = customtkinter.CTkLabel(master=frame_principal, text=dados, font=('Tahoma', 12))
            label_dados.pack(pady=5)

        nova_janela.after(2000, lambda: nova_janela.destroy())
        nova_janela.mainloop()

        nova_janela.mainloop()


    def seleciona_tripulante_por_cpf(self):
        cpf_selecionado = ""

        def confirmar():
            nonlocal cpf_selecionado
            cpf_selecionado = cpf_entry.get().strip()
            nova_janela.destroy()

        nova_janela = customtkinter.CTk()
        nova_janela.geometry(self.centralizar_janela(nova_janela, 300, 500))
        nova_janela.title("Selecionar Tripulante por CPF")

        frame_principal = customtkinter.CTkFrame(master=nova_janela, corner_radius=20, border_width=4, border_color='green')
        frame_principal.pack(pady=20, padx=60, fill='both', expand=True)

        label_titulo = customtkinter.CTkLabel(master=frame_principal, text="Selecionar Tripulante por CPF", font=('Tahoma', 16))
        label_titulo.pack(pady=12, padx=10)

        cpf_label = customtkinter.CTkLabel(master=frame_principal, text="CPF do tripulante que deseja selecionar:")
        cpf_label.pack(pady=5, padx=10)

        cpf_entry = customtkinter.CTkEntry(master=frame_principal)
        cpf_entry.pack(pady=5, padx=10)

        botao_confirmar = customtkinter.CTkButton(master=frame_principal, text="Confirmar", command=confirmar)
        botao_confirmar.pack(pady=10, padx=10)

        nova_janela.mainloop()
        return cpf_selecionado

    def voltar(self, nova_janela,):
        nova_janela.after(1000, nova_janela.destroy(),lambda: self.mostra_opcoes())