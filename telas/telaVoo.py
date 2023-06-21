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
        nova_janela.geometry('500x600')
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

    def pega_dados_voo(self) -> DadosIncluiVoo:
        print("-------- DADOS VOO ----------")

        while True:
            partida = input("Local de partida do Voo: ").upper().strip()

            if partida:
                break

            else:
                print("Dado invalido, digite novamente!!!")

        while True:
            destino = input("Local de destino do Voo: ").upper().strip()

            if destino:
                break

            else:
                print("Dado invalido, digite novamente!!!")

        while True:
            data_do_voo = input("Data do Voo (formato: DD/MM/AAAA): ").strip()

            try:
                data_do_voo = verifica_data(data_do_voo)
                break

            except ValueError:
                print("Dado invalido, digite novamente!!!")

        while True:
            modelo_aviao = (
                input("Modelo do Avião que realizará o Voo: ").upper().strip()
            )

            if modelo_aviao:
                break

            else:
                print("Dado invalido, digite novamente!!!")

        return {
            "partida": partida,
            "destino": destino,
            "data_do_voo": data_do_voo,
            "modelo_aviao": modelo_aviao,
        }

    def pega_dados_altera_voo(self) -> DadosAlteraVoo:
        print("-------- DADOS VOO ----------")

        partida = input("Local de partida do Voo: ").upper().strip()
        destino = input("Local de destino do Voo: ").upper().strip()

        while True:
            data_do_voo = input("Data do Voo (formato: DD/MM/AAAA): ").strip()

            if not data_do_voo:
                break

            try:
                data_do_voo = verifica_data(data_do_voo)
                break

            except Exception:
                print("Dado invalido, digite novamente!!!")

        return {
            "partida": partida,
            "destino": destino,
            "data_do_voo": data_do_voo,
        }

    def mostra_registro(self, dados_aviao: "dict[str, str | int]"):
        print("-------- LOG DE AÇÕES ----------")
        for index, valor in dados_aviao.items():
            print(f" {index} : {valor} ")
            print("--------------------------------")

    def mostra_voo(self, dados_voo: dict):
        for chave, valor in dados_voo.items():
            print(f"{chave}: {valor}")

        print("\n")

    def seleciona_voo(self):
        codigo = input("Insira o código do voo que deseja selecionar: ").upper()
        return codigo
