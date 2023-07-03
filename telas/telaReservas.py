import string
from typing import TypedDict
from telas.abstractTela import AbstractTela
from entidades.voo import Voo
import customtkinter


class DadosIncluiReserva(TypedDict):
    fileira: int
    letra: str
    cpf_passageiro: str
    codigo_voo: str


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
        # Configurações da interface gráfica
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('green')

    def mostra_opcoes(self) -> int:
        # Criar uma nova janela
        nova_janela = customtkinter.CTk()
        nova_janela.geometry(self.centralizar_janela(nova_janela, 500, 600))
        nova_janela.title("Tela Reservas")

        opcao_selecionada = None

        def set_opcao_selecionada(index: int):
            nonlocal opcao_selecionada
            opcao_selecionada = index
            nova_janela.destroy()

        frame = customtkinter.CTkFrame(master=nova_janela, corner_radius=20, border_width=4, border_color='green')
        frame.pack(pady=20, padx=60, fill='both', expand=True)

        label = customtkinter.CTkLabel(master=frame, text="RESERVAS", font=('Tahoma', 20))
        label.pack(pady=12, padx=10)

        for index, opcao in self.opcoes.items():
            button = customtkinter.CTkButton(master=frame, text=opcao, command=lambda index=index: set_opcao_selecionada(index))
            button.pack(pady=12, padx=10)

        nova_janela.mainloop()

        return opcao_selecionada


    def pega_cpf(self):
        # Criar uma nova janela
        nova_janela = customtkinter.CTk()
        nova_janela.geometry(self.centralizar_janela(nova_janela, 300, 500))
        nova_janela.title("CPF do Passageiro")

        # Criar o frame principal
        frame_principal = customtkinter.CTkFrame(master=nova_janela, corner_radius=20, border_width=4, border_color='green')
        frame_principal.pack(pady=20, padx=60, fill='both', expand=True)

        # Label de instrução
        label_instrucao = customtkinter.CTkLabel(master=frame_principal, text="Digite o CPF do passageiro:", font=('Tahoma', 14))
        label_instrucao.pack(pady=10)

        # Entrada de texto
        entry_cpf = customtkinter.CTkEntry(master=frame_principal, placeholder_text="CPF", width=200)
        entry_cpf.pack(pady=5)
        # Função de retorno
        def confirmar():
            global cpf
            cpf = entry_cpf.get().strip()

            try:
                self.verica_cpf(cpf)
                nova_janela.destroy()

            except Exception as e:
                mensagem_erro = customtkinter.CTkLabel(master=frame_principal, text=str(e), font=('Tahoma', 12))
                mensagem_erro.pack(pady=10)
                mensagem_erro.after(3000, lambda: mensagem_erro.destroy())
                nova_janela.after(3000, lambda: nova_janela.destroy(), self.mostra_opcoes())

        # Botão de confirmação
        button_confirmar = customtkinter.CTkButton(master=frame_principal, text="Confirmar", command=confirmar, width=10)
        button_confirmar.pack(pady=10)

        nova_janela.mainloop()
        return cpf

    def verica_cpf(self, cpf):
        if not cpf.isdigit():
            raise Exception("O CPF deve ser composto por dígitos!")

    def pega_voo(self):
        # Configurações da interface gráfica
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('green')

        # Criar uma nova janela
        nova_janela = customtkinter.CTk()
        nova_janela.geometry(self.centralizar_janela(nova_janela, 200, 500))
        nova_janela.title("Código do Voo")

        # Criar o frame principal
        frame_principal = customtkinter.CTkFrame(master=nova_janela, corner_radius=20, border_width=4, border_color='green')
        frame_principal.pack(pady=20, padx=60, fill='both', expand=True)

        # Label de instrução
        label_instrucao = customtkinter.CTkLabel(master=frame_principal, text="Digite o código do Voo:", font=('Tahoma', 14))
        label_instrucao.pack(pady=10)

        # Entrada de texto
        entry_codigo_voo = customtkinter.CTkEntry(master=frame_principal, placeholder_text="Código do Voo", width=200)
        entry_codigo_voo.pack(pady=5)

        # Função de retorno
        def confirmar():
            global codigo_voo
            codigo_voo = entry_codigo_voo.get().strip()
            
            if not codigo_voo:
                label_mensagem = customtkinter.CTkLabel(master=frame_principal, text="Codigo inválido, digite novamente!", font=('Tahoma', 12))
                label_mensagem.pack(pady=30)
                label_mensagem.after(4000, lambda: label_mensagem.destroy(), self.mostra_opcoes())
                return
            
            label_mensagem = customtkinter.CTkLabel(master=frame_principal, text="Dados inseridos com sucesso!", font=('Tahoma', 20))
            label_mensagem.pack(pady=50)
            nova_janela.update_idletasks()
            nova_janela.after(1000, nova_janela.destroy(),lambda: self.mostra_opcoes())

        # Botão de confirmação
        button_confirmar = customtkinter.CTkButton(master=frame_principal, text="Confirmar", command=confirmar, width=10)
        button_confirmar.pack(pady=10)

        nova_janela.mainloop()
        return codigo_voo

    def pega_fileira(self, alterando=False):
        # Configurações da interface gráfica
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('green')

        # Criar uma nova janela
        nova_janela = customtkinter.CTk()
        nova_janela.geometry(self.centralizar_janela(nova_janela, 200, 500))
        nova_janela.title("Número da Fileira")

        # Criar o frame principal
        frame_principal = customtkinter.CTkFrame(master=nova_janela, corner_radius=20, border_width=4, border_color='green')
        frame_principal.pack(pady=20, padx=60, fill='both', expand=True)

        # Label de instrução
        label_instrucao = customtkinter.CTkLabel(master=frame_principal, text="Digite o número da fileira desejada:", font=('Tahoma', 14))
        label_instrucao.pack(pady=10)

        # Entrada de texto
        entry_fileira = customtkinter.CTkEntry(master=frame_principal, placeholder_text="Número da Fileira", width=200)
        entry_fileira.pack(pady=5)

        # Função de retorno
        def confirmar():
            global fileira
            fileira = entry_fileira.get().strip()

            try:
                if not fileira and alterando:
                    nova_janela.destroy()
                    self.pega_fileira(0, alterando)
                else:
                    self.verica_fileira(fileira)
                    nova_janela.destroy()
                    self.pega_fileira(int(fileira), alterando)

            except Exception as e:
                mensagem_erro = customtkinter.CTkLabel(master=frame_principal, text=str(e), font=('Tahoma', 12))
                mensagem_erro.pack(pady=10)

        # Botão de confirmação
        button_confirmar = customtkinter.CTkButton(master=frame_principal, text="Confirmar", command=confirmar, width=10)
        button_confirmar.pack(pady=10)

        nova_janela.mainloop()
        return int(fileira)
    
    def verica_fileira(self, fileira):
        if not fileira.isdigit():
            raise Exception("A fileira deve ser composta por números!")

        if int(fileira) < 1:
            raise Exception("A fileira deve ser maior que 1!")

    def pega_assento_fileira(self, alterando=False):
        # Configurações da interface gráfica
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('green')

        # Criar uma nova janela
        nova_janela = customtkinter.CTk()
        nova_janela.geometry(self.centralizar_janela(nova_janela, 200, 500))
        nova_janela.title("Letra do Assento")

        # Criar o frame principal
        frame_principal = customtkinter.CTkFrame(master=nova_janela, corner_radius=20, border_width=4, border_color='green')
        frame_principal.pack(pady=20, padx=60, fill='both', expand=True)

        # Label de instrução
        label_instrucao = customtkinter.CTkLabel(master=frame_principal, text="Digite a letra do assento desejado:", font=('Tahoma', 14))
        label_instrucao.pack(pady=10)

        # Entrada de texto
        entry_assento = customtkinter.CTkEntry(master=frame_principal, placeholder_text="Letra do Assento", width=200)
        entry_assento.pack(pady=5)

        # Função de retorno
        def confirmar():
            global assento
            assento = entry_assento.get().strip()

            try:
                if not assento and alterando:
                    nova_janela.destroy()
                    self.pega_assento_fileira("", alterando)
                else:
                    self.verica_assento_fileira(assento)
                    nova_janela.destroy()
                    self.pega_assento_fileira(assento, alterando)

            except Exception as e:
                mensagem_erro = customtkinter.CTkLabel(master=frame_principal, text=str(e), font=('Tahoma', 12))
                mensagem_erro.pack(pady=10)

        # Botão de confirmação
        button_confirmar = customtkinter.CTkButton(master=frame_principal, text="Confirmar", command=confirmar, width=10)
        button_confirmar.pack(pady=10)

        nova_janela.mainloop()
        return assento

    def verica_assento_fileira(self, assento):
        if assento not in string.ascii_uppercase:
            raise Exception("O campo assento deve ser uma letra!")

    def mostra_reserva(self, dados_reserva: "dict[str, str]"):
        # Configurações da interface gráfica
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('green')

        # Criar uma nova janela
        nova_janela = customtkinter.CTk()
        nova_janela.geometry(self.centralizar_janela(nova_janela, 500, 600))
        nova_janela.title("Reserva")

        # Criar o frame principal
        frame_principal = customtkinter.CTkFrame(master=nova_janela, corner_radius=20, border_width=4, border_color='green')
        frame_principal.pack(pady=20, padx=60, fill='both', expand=True)

        # Label de título
        label_titulo = customtkinter.CTkLabel(master=frame_principal, text="Reserva:", font=('Tahoma', 20))
        label_titulo.pack(pady=10)

        # Criar um frame para os registros
        frame_registros = customtkinter.CTkFrame(master=frame_principal)
        frame_registros.pack(pady=10, padx=10, side='top', fill="both", expand=True)

        # Exibir os registros
        for chave, valor in dados_reserva.items():
            reserva_str = f"{chave}: {valor}"
            label_registro = customtkinter.CTkLabel(master=frame_registros, text=reserva_str, font=('Tahoma', 14))
            label_registro.pack(pady=5, padx=10, side='top', fill="both", expand=True)

        nova_janela.mainloop()

    def mostra_assentos_voo(self, voo):
        # Criar uma nova janela
        nova_janela = customtkinter.CTk()
        nova_janela.geometry(self.centralizar_janela(nova_janela, 300, 800))
        nova_janela.title("Assentos do Voo")

        # Criar o frame principal
        frame_principal = customtkinter.CTkFrame(master=nova_janela, corner_radius=20, border_width=4, border_color='green')
        frame_principal.pack(pady=20, padx=60, fill='both', expand=True)

        # Label de título
        label_titulo = customtkinter.CTkLabel(master=frame_principal, text="Assentos do Voo:", font=('Tahoma', 20))
        label_titulo.pack(pady=10)

        # Criar um frame para exibir os assentos
        frame_assentos = customtkinter.CTkFrame(master=frame_principal)
        frame_assentos.pack(pady=10, padx=10, side='top', fill="both", expand=True)

        # Cabeçalho das colunas
        label_cabecalho = customtkinter.CTkLabel(master=frame_assentos, text=" ", font=('Tahoma', 14))
        label_cabecalho.pack(side='left')

        for i in range(voo.aviao.assentos_por_fileira):
            label_cabecalho = customtkinter.CTkLabel(master=frame_assentos, text=string.ascii_uppercase[i], font=('Tahoma', 14))
            label_cabecalho.pack(side='left')

        # Exibir os assentos
        assentos_selecionados = []

        def confirmar():
            nonlocal assentos_selecionados
            assentos_selecionados = []

            # Percorrer todos os checkboxes e verificar os selecionados
            for fileira, fileira_checkboxes in enumerate(assentos_checkboxes):
                for coluna, checkbox in enumerate(fileira_checkboxes):
                    if checkbox.is_checked():
                        assento = f"{fileira + 1}{string.ascii_uppercase[coluna]}"
                        assentos_selecionados.append(assento)

            if len(assentos_selecionados) > 0:
                customtkinter.messagebox.showinfo("Assentos Selecionados", f"Assentos selecionados: {', '.join(assentos_selecionados)}")
            else:
                customtkinter.messagebox.showinfo("Nenhum Assento Selecionado", "Nenhum assento foi selecionado.")

        assentos_checkboxes = []

        for i in range(voo.aviao.fileiras):
            frame_fileira = customtkinter.CTkFrame(master=frame_assentos)
            frame_fileira.pack(side='top')

            label_fileira = customtkinter.CTkLabel(master=frame_fileira, text=str(i + 1), font=('Tahoma', 14))
            label_fileira.pack(side='left')

            fileira_checkboxes = []

            for j in range(voo.aviao.assentos_por_fileira):
                assento_checkbox = customtkinter.CTkCheckBox(master=frame_fileira, text=string.ascii_uppercase[j], width=10)
                assento_checkbox.pack(side='left')

                fileira_checkboxes.append(assento_checkbox)

            assentos_checkboxes.append(fileira_checkboxes)

        # Botão de confirmar
        btn_confirmar = customtkinter.CTkButton(master=frame_principal, text="Confirmar", command=confirmar)
        btn_confirmar.pack(pady=10)

        nova_janela.mainloop()

        return assentos_selecionados





    def seleciona_reserva(self) -> str:
        # Configurações da interface gráfica
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('green')

        # Criar uma nova janela
        nova_janela = customtkinter.CTk()
        nova_janela.geometry(self.centralizar_janela(nova_janela, 200, 500))
        nova_janela.title("Código da Reserva")

        # Criar o frame principal
        frame_principal = customtkinter.CTkFrame(master=nova_janela, corner_radius=20, border_width=4, border_color='green')
        frame_principal.pack(pady=20, padx=60, fill='both', expand=True)

        # Label de instrução
        label_instrucao = customtkinter.CTkLabel(master=frame_principal, text="Insira o código da reserva que deseja buscar:", font=('Tahoma', 14))
        label_instrucao.pack(pady=10)

        # Entrada de texto
        entry_codigo_reserva = customtkinter.CTkEntry(master=frame_principal, placeholder_text="Código da Reserva", width=200)
        entry_codigo_reserva.pack(pady=5)

        # Função de retorno
        def confirmar():
            global codigo_reserva
            codigo_reserva = entry_codigo_reserva.get().strip()
            
            if not codigo_reserva:
                label_mensagem = customtkinter.CTkLabel(master=frame_principal, text="Codigo inválido, digite novamente!", font=('Tahoma', 12))
                label_mensagem.pack(pady=30)
                label_mensagem.after(4000, lambda: label_mensagem.destroy(), self.mostra_opcoes())
                return
        
            label_mensagem = customtkinter.CTkLabel(master=frame_principal, text="Dados inseridos com sucesso!", font=('Tahoma', 20))
            label_mensagem.pack(pady=50)
            nova_janela.update_idletasks()
            nova_janela.after(1000, nova_janela.destroy(),lambda: self.mostra_opcoes())

        # Botão de confirmação
        button_confirmar = customtkinter.CTkButton(master=frame_principal, text="Confirmar", command=confirmar, width=10)
        button_confirmar.pack(pady=10)

        nova_janela.mainloop()
        return codigo_reserva