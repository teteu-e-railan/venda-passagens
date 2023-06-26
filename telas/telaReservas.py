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

    def mostra_opcoes(self) -> int:
        # Configurações da interface gráfica
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('green')

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


    def pega_cpf(self, alterando=False):
        # Configurações da interface gráfica
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('green')

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
            codigo_voo = entry_codigo_voo.get().strip()
            nova_janela.destroy()
            self.operacao_pega_voo(codigo_voo)

        # Botão de confirmação
        button_confirmar = customtkinter.CTkButton(master=frame_principal, text="Confirmar", command=confirmar, width=10)
        button_confirmar.pack(pady=10)

        nova_janela.mainloop()

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
            fileira = entry_fileira.get().strip()

            try:
                if not fileira and alterando:
                    nova_janela.destroy()
                    self.operacao_pega_fileira(0, alterando)
                else:
                    self.verica_fileira(fileira)
                    nova_janela.destroy()
                    self.operacao_pega_fileira(int(fileira), alterando)

            except Exception as e:
                mensagem_erro = customtkinter.CTkLabel(master=frame_principal, text=str(e), font=('Tahoma', 12))
                mensagem_erro.pack(pady=10)

        # Botão de confirmação
        button_confirmar = customtkinter.CTkButton(master=frame_principal, text="Confirmar", command=confirmar, width=10)
        button_confirmar.pack(pady=10)

        nova_janela.mainloop()

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
            assento = entry_assento.get().strip()

            try:
                if not assento and alterando:
                    nova_janela.destroy()
                    self.operacao_pega_assento_fileira("", alterando)
                else:
                    self.verica_assento_fileira(assento)
                    nova_janela.destroy()
                    self.operacao_pega_assento_fileira(assento, alterando)

            except Exception as e:
                mensagem_erro = customtkinter.CTkLabel(master=frame_principal, text=str(e), font=('Tahoma', 12))
                mensagem_erro.pack(pady=10)

        # Botão de confirmação
        button_confirmar = customtkinter.CTkButton(master=frame_principal, text="Confirmar", command=confirmar, width=10)
        button_confirmar.pack(pady=10)

        nova_janela.mainloop()

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
        # Configurações da interface gráfica
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('green')

        # Criar uma nova janela
        nova_janela = customtkinter.CTk()
        nova_janela.geometry(self.centralizar_janela(nova_janela, 500, 600))
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
        label_cabecalho = customtkinter.CTkLabel(master=frame_assentos, text="{:<1}".format(""), font=('Tahoma', 14))
        label_cabecalho.pack(side='top')

        for i in range(voo.aviao.assentos_por_fileira):
            label_cabecalho = customtkinter.CTkLabel(master=frame_assentos, text="[{:1}] |".format(string.ascii_uppercase[i]), font=('Tahoma', 14))
            label_cabecalho.pack(side='top')

        # Exibir os assentos
        for i in range(voo.aviao.fileiras):
            label_fileira = customtkinter.CTkLabel(master=frame_assentos, text="{} ".format(i + 1), font=('Tahoma', 14))
            label_fileira.pack(side='top')

            for j in range(voo.aviao.assentos_por_fileira):
                label_assento = customtkinter.CTkLabel(master=frame_assentos, text="[{:1}] |".format(voo.assentos[i][j]), font=('Tahoma', 14))
                label_assento.pack(side='top')

        nova_janela.mainloop()

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
            codigo_reserva = entry_codigo_reserva.get().strip()
            nova_janela.destroy()
            self.operacao_seleciona_reserva(codigo_reserva)

        # Botão de confirmação
        button_confirmar = customtkinter.CTkButton(master=frame_principal, text="Confirmar", command=confirmar, width=10)
        button_confirmar.pack(pady=10)

        nova_janela.mainloop()
