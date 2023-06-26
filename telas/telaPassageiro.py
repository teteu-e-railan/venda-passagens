from telas.abstractTela import AbstractTela
import customtkinter


class TelaPassagerio(AbstractTela):
    def __init__(self):
        super().__init__(
            {
                1: "Incluir Passageiro",
                2: "Alterar Passageiro",
                3: "Listar Passageiros",
                4: "Excluir Passageiro",
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
        nova_janela.geometry(self.centralizar_janela(nova_janela,500, 600))
        nova_janela.title("Tela Passageiro")

        opcao_selecionada = None

        def set_opcao_selecionada(index: int):
            nonlocal opcao_selecionada
            opcao_selecionada = index
            nova_janela.destroy()

        frame = customtkinter.CTkFrame(master=nova_janela, corner_radius=20, border_width=4, border_color='green')
        frame.pack(pady=20, padx=60, fill='both', expand=True)

        label = customtkinter.CTkLabel(master=frame, text="Passageiros", font=('Tahoma', 20))
        label.pack(pady=12, padx=10)

        for index, opcao in self.opcoes.items():
            button = customtkinter.CTkButton(master=frame, text=opcao, command=lambda index=index: set_opcao_selecionada(index))
            button.pack(pady=12, padx=10)

        nova_janela.mainloop()

        return opcao_selecionada

    def pega_dados_passageiro(self):
        # Configurações da interface gráfica
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('green')

        # Criar uma nova janela
        nova_janela = customtkinter.CTk()
        nova_janela.geometry(self.centralizar_janela(nova_janela,500, 600))
        nova_janela.title("Tela Passageiro")


        dados = {}

        def confirmar():
            nonlocal dados
            nome = entry_nome.get().strip()
            cpf = entry_cpf.get().strip()
            idade = entry_idade.get().strip()
            telefone = entry_telefone.get().strip()

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

            label_mensagem = customtkinter.CTkLabel(master=frame, text="Dados inseridos com sucesso!", font=('Tahoma', 20),)
            label_mensagem.pack(pady=50)
            nova_janela.update_idletasks()
            nova_janela.after(1000, nova_janela.destroy(),lambda: self.mostra_opcoes())

        frame = customtkinter.CTkFrame(master=nova_janela, corner_radius=20, border_width=4, border_color='green')
        frame.pack(pady=20, padx=60, fill='both', expand=True)

        label = customtkinter.CTkLabel(master=frame, text="Inserir Dados do Passageiro", font=('Tahoma', 20))  
        label.pack(pady=12, padx=10)

        entry_nome = customtkinter.CTkEntry(master=frame, placeholder_text="Digite o nome", width=200)
        entry_nome.pack(pady=5)

        entry_cpf = customtkinter.CTkEntry(master=frame, placeholder_text="Digite o CPF", width=200)
        entry_cpf.pack(pady=5)

        entry_idade = customtkinter.CTkEntry(master=frame, placeholder_text="Digite a idade", width=200)
        entry_idade.pack(pady=5)

        entry_telefone = customtkinter.CTkEntry(master=frame, placeholder_text="Digite o telefone", width=200)
        entry_telefone.pack(pady=5)
        
        button_confirmar = customtkinter.CTkButton(master=frame, text="Confirmar", command=confirmar, width=10)
        button_confirmar.pack(pady=10)

        nova_janela.mainloop()

        return dados

    def altera_dados_passageiro(self):
        # Configurações da interface gráfica
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('green')

        # Criar uma nova janela
        nova_janela = customtkinter.CTk()
        nova_janela.geometry(self.centralizar_janela(nova_janela,500, 600))
        nova_janela.title("Tela Passageiro")

        dados = {}

        def confirmar():
            nonlocal dados
            nome = entry_nome.get().strip()
            cpf = entry_cpf.get().strip()
            idade = entry_idade.get().strip()
            telefone = entry_telefone.get().strip()

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

            label_mensagem = customtkinter.CTkLabel(master=frame, text="Dados inseridos com sucesso!", font=('Tahoma', 20))
            label_mensagem.pack(pady=50)
            nova_janela.update_idletasks()
            nova_janela.after(1000, nova_janela.destroy(),lambda: self.mostra_opcoes())

        frame = customtkinter.CTkFrame(master=nova_janela, corner_radius=20, border_width=4, border_color='green')
        frame.pack(pady=20, padx=60, fill='both', expand=True)

        label = customtkinter.CTkLabel(master=frame, text="Alterar Dados do Passageiro", font=('Tahoma', 20))
        label.pack(pady=12, padx=10, fill='both', expand=True)

        entry_nome = customtkinter.CTkEntry(master=frame, placeholder_text="Digite o nome", width=200)
        entry_nome.pack(pady=5)

        entry_cpf = customtkinter.CTkEntry(master=frame, placeholder_text="Digite o CPF", width=200)
        entry_cpf.pack(pady=5)

        entry_idade = customtkinter.CTkEntry(master=frame, placeholder_text="Digite a idade", width=200)
        entry_idade.pack(pady=5)

        entry_telefone = customtkinter.CTkEntry(master=frame, placeholder_text="Digite o telefone", width=200)
        entry_telefone.pack(pady=5)

        button_confirmar = customtkinter.CTkButton(master=frame, text="Confirmar", command=confirmar, width=10)
        button_confirmar.pack(pady=10)

        nova_janela.mainloop()

        return dados

    def mostra_registro(self, dados_aviao):
        # Configurações da interface gráfica
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('blue')

        # Criar uma nova janela
        nova_janela = customtkinter.CTk()
        nova_janela.geometry(self.centralizar_janela(nova_janela, 500, 600))
        nova_janela.title("Registros")

        # Criar o frame principal
        frame_principal = customtkinter.CTkFrame(master=nova_janela, corner_radius=20, border_width=4, border_color='green')
        frame_principal.pack(pady=20, padx=60, fill='both', expand=True)

        # Verificar se há registros para exibir
        if not dados_aviao:
            label_mensagem = customtkinter.CTkLabel(master=frame_principal, text="Sem registros encontrados", font=('Tahoma', 14))
            label_mensagem.pack(pady=50, padx=10, side='top', fill="both", expand=True)
        else:
            label_titulo = customtkinter.CTkLabel(master=frame_principal, text="Registros de Avião", font=('Tahoma', 20))
            label_titulo.pack(pady=12, padx=10, side='top', fill="both", expand=True)

            # Criar um frame para os registros
            frame_registros = customtkinter.CTkFrame(master=frame_principal)
            frame_registros.pack(pady=10, padx=10, side='top', fill="both", expand=True)

            # Exibir os registros
            for index, valor in dados_aviao.items():
                registro_str = f"{index}: {valor}"
                label_registro = customtkinter.CTkLabel(master=frame_registros, text=registro_str, font=('Tahoma', 14))
                label_registro.pack(pady=5, padx=10, side='top', fill="both", expand=True)
        botao_voltar = customtkinter.CTkButton(master=frame_principal, text="Voltar", command=nova_janela.destroy)
        botao_voltar.pack(pady=10)
        nova_janela.mainloop()

    def mostra_passageiro(self, dados_passageiro):
        # Configurações da interface gráfica
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('green')

        # Criar uma nova janela
        nova_janela = customtkinter.CTk()
        nova_janela.geometry(self.centralizar_janela(nova_janela, 500, 600))
        nova_janela.title("Passageiro")

        # Criar o frame principal
        frame_principal = customtkinter.CTkFrame(master=nova_janela, corner_radius=20, border_width=4, border_color='green')
        frame_principal.pack(pady=20, padx=60, fill='both', expand=True)

        # Verificar se há registros para exibir
        if not dados_passageiro:
            label_mensagem = customtkinter.CTkLabel(master=frame_principal, text="Sem registros encontrados", font=('Tahoma', 14))
            label_mensagem.pack(pady=50, padx=10, side='top', fill="both", expand=True)
        else:
            label_titulo = customtkinter.CTkLabel(master=frame_principal, text="Passageiros cadastrados", font=('Tahoma', 20))
            label_titulo.pack(pady=12, padx=10, side='top', fill="both", expand=True)

            # Criar um frame para os registros
            frame_registros = customtkinter.CTkFrame(master=frame_principal)
            frame_registros.pack(pady=10, padx=10, side='top', fill="both", expand=True)

            # Exibir os registros
            contador = 1
            for chave, valor in dados_passageiro.items():
                passageiro_str = f"{contador} - {chave}: {valor}"
                label_registro = customtkinter.CTkLabel(master=frame_registros, text=passageiro_str, font=('Tahoma', 14))
                label_registro.pack(pady=5, padx=10, side='top', fill="both", expand=True)
                contador += 1

        nova_janela.after(2000, lambda: nova_janela.destroy())
        nova_janela.mainloop()

    def seleciona_passageiro_por_cpf(self):
        cpf_selecionado = ""

        def confirmar():
            nonlocal cpf_selecionado
            cpf_selecionado = entry_cpf.get().strip()
            nova_janela.destroy()

        nova_janela = customtkinter.CTk()
        nova_janela.geometry(self.centralizar_janela(nova_janela,300, 400))
        nova_janela.title("Selecionar Passageiro por CPF")

        frame = customtkinter.CTkFrame(master=nova_janela, corner_radius=10, border_width=4, border_color='green')
        frame.pack(pady=20, padx=40)

        label = customtkinter.CTkLabel(master=frame, text="CPF do passageiro que deseja selecionar:")
        label.pack(pady=10)

        entry_cpf = customtkinter.CTkEntry(master=frame, width=90)
        entry_cpf.pack(pady=5)

        button_confirmar = customtkinter.CTkButton(master=frame, text="Confirmar", command=confirmar)
        button_confirmar.pack(pady=10)

        nova_janela.mainloop()

        return cpf_selecionado


    # Botão "Voltar"
    def voltar(self, nova_janela,):
        nova_janela.after(1000, nova_janela.destroy(),lambda: self.mostra_opcoes())
