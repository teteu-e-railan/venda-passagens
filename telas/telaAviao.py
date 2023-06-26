from telas.abstractTela import AbstractTela
import customtkinter
import customtkinter as ctk

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

    def mostra_opcoes(self) -> int:
        # Configurações da interface gráfica
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('green')

        # Criar uma nova janela
        nova_janela = customtkinter.CTk()
        nova_janela.geometry(self.centralizar_janela(nova_janela, 500, 600))
        nova_janela.title("Tela aviao")

        opcao_selecionada = None

        def set_opcao_selecionada(index: int):
            nonlocal opcao_selecionada
            opcao_selecionada = index
            nova_janela.destroy()

        frame = customtkinter.CTkFrame(master=nova_janela, corner_radius=20, border_width=4, border_color='green')
        frame.pack(pady=20, padx=60, fill='both', expand=True)

        label = customtkinter.CTkLabel(master=frame, text="Aviões", font=('Tahoma', 20))
        label.pack(pady=12, padx=10)

        for index, opcao in self.opcoes.items():
            button = customtkinter.CTkButton(master=frame, text=opcao, command=lambda index=index: set_opcao_selecionada(index))
            button.pack(pady=12, padx=10)

        nova_janela.mainloop()

        return opcao_selecionada

    def pega_dados_aviao(self):
        # Configurações da interface gráfica
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('green')

        # Criar uma nova janela
        nova_janela = customtkinter.CTk()
        nova_janela.geometry(self.centralizar_janela(nova_janela, 500, 600))
        nova_janela.title("Tela Avião")

        dados = {}

        def confirmar():
            nonlocal dados
            modelo = entry_modelo.get().strip().upper()
            fileiras = entry_fileiras.get().strip()
            assentos_por_fileira = entry_assentos.get().strip()

            # Validar os dados
            if not modelo:
                label_mensagem = customtkinter.CTkLabel(master=frame, text="Modelo inválido, digite novamente!", font=('Tahoma', 12))
                label_mensagem.pack(pady=30)
                label_mensagem.after(4000, lambda: label_mensagem.destroy())
                return

            if not fileiras or not fileiras.isdigit():
                label_mensagem = customtkinter.CTkLabel(master=frame, text="Número de fileiras inválido, digite novamente!", font=('Tahoma', 12))
                label_mensagem.pack(pady=10)
                label_mensagem.after(4000, lambda: label_mensagem.destroy())
                return

            if not assentos_por_fileira or not assentos_por_fileira.isdigit():
                label_mensagem = customtkinter.CTkLabel(master=frame, text="Número de assentos por fileira inválido, digite novamente!", font=('Tahoma', 12))
                label_mensagem.pack(pady=10)
                label_mensagem.after(4000, lambda: label_mensagem.destroy())
                return

            # Armazenar os dados
            dados["modelo"] = modelo
            dados["fileiras"] = int(fileiras)
            dados["assentos_por_fileira"] = int(assentos_por_fileira)

            label_mensagem = customtkinter.CTkLabel(master=frame, text="Dados inseridos com sucesso!", font=('Tahoma', 20))
            label_mensagem.pack(pady=50)
            nova_janela.update_idletasks()
            nova_janela.after(1000, nova_janela.destroy(), lambda: self.mostra_opcoes())

        frame = customtkinter.CTkFrame(master=nova_janela, corner_radius=20, border_width=4, border_color='green')
        frame.pack(pady=20, padx=60, fill='both', expand=True)

        label = customtkinter.CTkLabel(master=frame, text="Inserir Dados do Avião", font=('Tahoma', 20))
        label.pack(pady=12, padx=10)

        entry_modelo = customtkinter.CTkEntry(master=frame, placeholder_text="Digite o modelo", width=200)
        entry_modelo.pack(pady=5)

        entry_fileiras = customtkinter.CTkEntry(master=frame, placeholder_text="Digite o número de fileiras", width=200)
        entry_fileiras.pack(pady=5)

        entry_assentos = customtkinter.CTkEntry(master=frame, placeholder_text="Digite o número de assentos por fileira", width=200)
        entry_assentos.pack(pady=5)

        button_confirmar = customtkinter.CTkButton(master=frame, text="Confirmar", command=confirmar, width=10)
        button_confirmar.pack(pady=10)

        nova_janela.mainloop()

        return dados


    def altera_dados_passageiro(self):
        # Configurações da interface gráfica
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('green')

        # Criar uma nova janela
        nova_janela = ctk.CTk()
        nova_janela.geometry(self.centralizar_janela(nova_janela, 500, 600))
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
                label_mensagem = ctk.CTkLabel(master=frame, text="Nome inválido, digite novamente!", font=('Tahoma', 12))
                label_mensagem.pack(pady=30)
                label_mensagem.after(4000, lambda: label_mensagem.destroy())
                return

            try:
                int(cpf)
            except ValueError:
                label_mensagem = ctk.CTkLabel(master=frame, text="CPF inválido, digite novamente!", font=('Tahoma', 12))
                label_mensagem.pack(pady=10)
                label_mensagem.after(4000, lambda: label_mensagem.destroy())
                return

            if not idade:
                label_mensagem = ctk.CTkLabel(master=frame, text="Idade inválida, digite novamente!", font=('Tahoma', 12))
                label_mensagem.pack(pady=10)
                label_mensagem.after(4000, lambda: label_mensagem.destroy())
                return

            try:
                int(idade)
            except ValueError:
                label_mensagem = ctk.CTkLabel(master=frame, text="Idade inválida, digite novamente!", font=('Tahoma', 12))
                label_mensagem.pack(pady=10)
                label_mensagem.after(4000, lambda: label_mensagem.destroy())
                return

            try:
                int(telefone)
            except ValueError:
                label_mensagem = ctk.CTkLabel(master=frame, text="Telefone inválido, digite novamente!", font=('Tahoma', 12))
                label_mensagem.pack(pady=10)
                label_mensagem.after(1000, lambda: label_mensagem.destroy())
                return

            # Armazenar os dados
            dados["nome"] = nome
            dados["cpf"] = cpf
            dados["idade"] = idade
            dados["telefone"] = telefone

            label_mensagem = ctk.CTkLabel(master=frame, text="Dados inseridos com sucesso!", font=('Tahoma', 20))
            label_mensagem.pack(pady=50)
            nova_janela.update_idletasks()
            nova_janela.after(1000, nova_janela.destroy(), lambda: self.mostra_opcoes())

        frame = ctk.CTkFrame(master=nova_janela, corner_radius=20, border_width=4, border_color='green')
        frame.pack(pady=20, padx=60, fill='both', expand=True)

        label = ctk.CTkLabel(master=frame, text="Alterar Dados do Passageiro", font=('Tahoma', 20))
        label.pack(pady=12, padx=10, fill='both', expand=True)

        entry_nome = ctk.CTkEntry(master=frame, placeholder_text="Digite o nome", width=200)
        entry_nome.pack(pady=5)

        entry_cpf = ctk.CTkEntry(master=frame, placeholder_text="Digite o CPF", width=200)
        entry_cpf.pack(pady=5)

        entry_idade = ctk.CTkEntry(master=frame, placeholder_text="Digite a idade", width=200)
        entry_idade.pack(pady=5)

        entry_telefone = ctk.CTkEntry(master=frame, placeholder_text="Digite o telefone", width=200)
        entry_telefone.pack(pady=5)

        button_confirmar = ctk.CTkButton(master=frame, text="Confirmar", command=confirmar, width=10)
        button_confirmar.pack(pady=10)

        nova_janela.mainloop()

        return dados

    def mostra_aviao(self, dados_aviao):
        # Configurações da interface gráfica
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('green')

        # Criar uma nova janela
        nova_janela = ctk.CTk()
        nova_janela.geometry(self.centralizar_janela(nova_janela, 500, 600))
        nova_janela.title("Avião")

        # Criar o frame principal
        frame_principal = ctk.CTkFrame(master=nova_janela, corner_radius=20, border_width=4, border_color='green')
        frame_principal.pack(pady=20, padx=60, fill='both', expand=True)

        # Verificar se há registros para exibir
        if not dados_aviao:
            label_mensagem = ctk.CTkLabel(master=frame_principal, text="Sem registros encontrados", font=('Tahoma', 14))
            label_mensagem.pack(pady=50, padx=10, side='top', fill="both", expand=True)
        else:
            label_titulo = ctk.CTkLabel(master=frame_principal, text="Aviões cadastrados", font=('Tahoma', 20))
            label_titulo.pack(pady=12, padx=10, side='top', fill="both", expand=True)

            # Criar um frame para os registros
            frame_registros = ctk.CTkFrame(master=frame_principal)
            frame_registros.pack(pady=10, padx=10, side='top', fill="both", expand=True)

            # Exibir os registros
            for chave, valor in dados_aviao.items():
                aviao_str = f"{chave}: {valor}"
                label_registro = ctk.CTkLabel(master=frame_registros, text=aviao_str, font=('Tahoma', 14))
                label_registro.pack(pady=5, padx=10, side='top', fill="both", expand=True)

        nova_janela.after(2000, lambda: nova_janela.destroy())
        nova_janela.mainloop()


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

    def mostra_modelo(self, avioes):
        # Configurações da interface gráfica
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('green')

        # Criar uma nova janela
        nova_janela = ctk.CTk()
        nova_janela.geometry(self.centralizar_janela(nova_janela, 500, 600))
        nova_janela.title("Modelos de Avião")

        # Criar o frame principal
        frame_principal = ctk.CTkFrame(master=nova_janela, corner_radius=20, border_width=4, border_color='green')
        frame_principal.pack(pady=20, padx=60, fill='both', expand=True)

        # Verificar se há registros para exibir
        if not avioes:
            label_mensagem = ctk.CTkLabel(master=frame_principal, text="Sem registros encontrados", font=('Tahoma', 14))
            label_mensagem.pack(pady=50, padx=10, side='top', fill="both", expand=True)
        else:
            label_titulo = ctk.CTkLabel(master=frame_principal, text="Modelos de Avião Disponíveis", font=('Tahoma', 20))
            label_titulo.pack(pady=12, padx=10, side='top', fill="both", expand=True)

            # Criar um frame para os registros
            frame_registros = ctk.CTkFrame(master=frame_principal)
            frame_registros.pack(pady=10, padx=10, side='top', fill="both", expand=True)

            # Exibir os registros
            for aviao in avioes:
                modelo_str = aviao.modelo
                label_registro = ctk.CTkLabel(master=frame_registros, text=modelo_str, font=('Tahoma', 14))
                label_registro.pack(pady=5, padx=10, side='top', fill="both", expand=True)

        nova_janela.after(2000, lambda: nova_janela.destroy())
        nova_janela.mainloop()

    def seleciona_aviao(self):
        # Configurações da interface gráfica
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('green')

        # Criar uma nova janela
        nova_janela = ctk.CTk()
        nova_janela.geometry(self.centralizar_janela(nova_janela, 200, 500))
        nova_janela.title("Selecionar Avião")

        # Criar o frame principal
        frame_principal = ctk.CTkFrame(master=nova_janela, corner_radius=20, border_width=4, border_color='green')
        frame_principal.pack(pady=20, padx=60, fill='both', expand=True)

        # Label de instrução
        label_instrucao = ctk.CTkLabel(master=frame_principal, text="Digite o modelo do avião que deseja selecionar:", font=('Tahoma', 14))
        label_instrucao.pack(pady=10)

        # Entrada de texto
        entry_modelo = ctk.CTkEntry(master=frame_principal, placeholder_text="Modelo", width=200)
        entry_modelo.pack(pady=5)

        # Função de retorno
        def confirmar():
            modelo = entry_modelo.get().strip()
            nova_janela.destroy()
            self.operacao_seleciona_aviao(modelo)

        # Botão de confirmação
        button_confirmar = ctk.CTkButton(master=frame_principal, text="Confirmar", command=confirmar, width=10)
        button_confirmar.pack(pady=10)

        nova_janela.mainloop()
