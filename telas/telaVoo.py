from typing import TypedDict, Literal
from datetime import datetime
from telas.abstractTela import AbstractTela
from helpers.verifica_data import verifica_data
import customtkinter


class DadosIncluiVoo(TypedDict):
    partida: str
    destino: str
    data_do_voo: datetime
    modelo_aviao: str


class DadosAlteraVoo(TypedDict):
    partida: str
    destino: str
    data_do_voo: "datetime | Literal['']"


class TelaVoo(AbstractTela):
    def __init__(self):
        super().__init__(
            {
                1: "Incluir Voo",
                2: "Alterar Voo",
                3: "Listar Voos",
                4: "Excluir Voo",
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
        nova_janela.title("Tela do sistema")

        opcao_selecionada = None

        def set_opcao_selecionada(index: int):
            nonlocal opcao_selecionada
            opcao_selecionada = index
            nova_janela.destroy()

        frame = customtkinter.CTkFrame(master=nova_janela, corner_radius=20, border_width=4, border_color='green')
        frame.pack(pady=20, padx=60, fill='both', expand=True)

        label = customtkinter.CTkLabel(master=frame, text="Voos", font=('Tahoma', 20))
        label.pack(pady=12, padx=10)

        for index, opcao in self.opcoes.items():
            button = customtkinter.CTkButton(master=frame, text=opcao, command=lambda index=index: set_opcao_selecionada(index))
            button.pack(pady=12, padx=10)

        nova_janela.mainloop()

        return opcao_selecionada

    def pega_dados_voo(self) -> dict:
        nova_janela = customtkinter.CTk()
        nova_janela.geometry(self.centralizar_janela(nova_janela, 500, 600))
        nova_janela.title("Dados do Voo")

        frame_principal = customtkinter.CTkFrame(master=nova_janela, corner_radius=20, border_width=4, border_color='green')
        frame_principal.pack(pady=20, padx=60, fill='both', expand=True)

        label_titulo = customtkinter.CTkLabel(master=frame_principal, text="Dados do Voo", font=('Tahoma', 16))
        label_titulo.pack(pady=12, padx=10, side='top')

        partida_entry = customtkinter.CTkEntry(master=frame_principal, placeholder_text="Local de partida do Voo:", width=200)
        partida_entry.pack(pady=10, padx=10)

        destino_entry = customtkinter.CTkEntry(master=frame_principal, placeholder_text="Local de destino do Voo:", width=200)
        destino_entry.pack(pady=10, padx=10)

        data_entry = customtkinter.CTkEntry(master=frame_principal, placeholder_text="Data do Voo (formato: DD/MM/AAAA):", width=200)
        data_entry.pack(pady=10, padx=10)

        modelo_entry = customtkinter.CTkEntry(master=frame_principal, placeholder_text="Modelo do Avião que realizará o Voo:", width=200)
        modelo_entry.pack(pady=10, padx=10)

        def confirmar():
            partida = partida_entry.get()
            destino = destino_entry.get()
            data_do_voo = data_entry.get()
            modelo_aviao = modelo_entry.get()

            if partida and destino and data_do_voo and modelo_aviao:
                nova_janela.destroy()
                self.operacao_pega_dados_voo({
                    "partida": partida,
                    "destino": destino,
                    "data_do_voo": data_do_voo,
                    "modelo_aviao": modelo_aviao
                })

        botao_confirmar = customtkinter.CTkButton(master=frame_principal, text="Confirmar", command=confirmar)
        botao_confirmar.pack(pady=10, padx=10)

        nova_janela.mainloop()

    def pega_dados_altera_voo(self) -> dict:
        nova_janela = customtkinter.CTk()
        nova_janela.geometry(self.centralizar_janela(nova_janela, 500, 600))
        nova_janela.title("Dados do Voo")

        frame_principal = customtkinter.CTkFrame(master=nova_janela, corner_radius=20, border_width=4, border_color='blue')
        frame_principal.pack(pady=20, padx=60, fill='both', expand=True)

        label_titulo = customtkinter.CTkLabel(master=frame_principal, text="Dados do Voo", font=('Tahoma', 16))
        label_titulo.pack(pady=12, padx=10, side='top')

        partida_entry = customtkinter.CTkEntry(master=frame_principal, text="Local de partida do Voo:")
        partida_entry.pack(pady=10, padx=10)

        destino_entry = customtkinter.CTkEntry(master=frame_principal, text="Local de destino do Voo:")
        destino_entry.pack(pady=10, padx=10)

        data_entry = customtkinter.CTkEntry(master=frame_principal, text="Data do Voo (formato: DD/MM/AAAA):")
        data_entry.pack(pady=10, padx=10)

        def confirmar():
            partida = partida_entry.get()
            destino = destino_entry.get()
            data_do_voo = data_entry.get()

            nova_janela.destroy()
            self.operacao_pega_dados_altera_voo({
                "partida": partida,
                "destino": destino,
                "data_do_voo": data_do_voo
            })

        botao_confirmar = customtkinter.CTkButton(master=frame_principal, text="Confirmar", command=confirmar)
        botao_confirmar.pack(pady=10, padx=10)

        nova_janela.mainloop()

    def mostra_registro(self, dados_aviao: dict):
        nova_janela = customtkinter.CTk()
        nova_janela.geometry(self.centralizar_janela(nova_janela, 500, 600))
        nova_janela.title("Log de Ações")

        frame_principal = customtkinter.CTkFrame(master=nova_janela, corner_radius=20, border_width=4, border_color='blue')
        frame_principal.pack(pady=20, padx=60, fill='both', expand=True)

        label_titulo = customtkinter.CTkLabel(master=frame_principal, text="Log de Ações", font=('Tahoma', 16))
        label_titulo.pack(pady=12, padx=10, side='top')

        for index, valor in dados_aviao.items():
            registro_str = f"{index}: {valor}"
            label_registro = customtkinter.CTkLabel(master=frame_principal, text=registro_str, font=('Tahoma', 12))
            label_registro.pack(pady=5, padx=10, side='top')

        nova_janela.mainloop()

    def mostra_voo(self, dados_voo: dict):
        nova_janela = customtkinter.CTk()
        nova_janela.geometry(self.centralizar_janela(nova_janela, 500, 600))
        nova_janela.title("Dados do Voo")

        frame_principal = customtkinter.CTkFrame(master=nova_janela, corner_radius=20, border_width=4, border_color='blue')
        frame_principal.pack(pady=20, padx=60, fill='both', expand=True)

        label_titulo = customtkinter.CTkLabel(master=frame_principal, text="Dados do Voo", font=('Tahoma', 16))
        label_titulo.pack(pady=12, padx=10, side='top')

        for index, valor in dados_voo.items():
            registro_str = f"{index}: {valor}"
            label_registro = customtkinter.CTkLabel(master=frame_principal, text=registro_str, font=('Tahoma', 12))
            label_registro.pack(pady=5, padx=10, side='top')

        nova_janela.mainloop()

    def seleciona_voo(self) -> str:
        nova_janela = customtkinter.CTk()
        nova_janela.geometry(self.centralizar_janela(nova_janela, 200, 500))
        nova_janela.title("Selecionar Voo")

        frame_principal = customtkinter.CTkFrame(master=nova_janela, corner_radius=20, border_width=4, border_color='blue')
        frame_principal.pack(pady=20, padx=60, fill='both', expand=True)

        label_titulo = customtkinter.CTkLabel(master=frame_principal, text="Selecionar Voo", font=('Tahoma', 16))
        label_titulo.pack(pady=12, padx=10, side='top')

        codigo_entry = customtkinter.CTkEntry(master=frame_principal, text="Insira o código do voo que deseja selecionar:")
        codigo_entry.pack(pady=10, padx=10)

        def confirmar():
            codigo = codigo_entry.get()
            nova_janela.destroy()
            self.operacao_seleciona_voo(codigo)

        botao_confirmar = customtkinter.CTkButton(master=frame_principal, text="Confirmar", command=confirmar)
        botao_confirmar.pack(pady=10, padx=10)

        nova_janela.mainloop()

