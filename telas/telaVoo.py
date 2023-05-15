from typing import TypedDict
from telas.abstractTela import AbstractTela
from helpers.verifica_data import verifica_data


class DadosIncluiVoo(TypedDict):
    partida: str
    destino: str
    data_do_voo: str
    modelo_aviao: str


class DadosAlteraVoo(TypedDict):
    partida: str
    destino: str
    data_do_voo: str


class TelaVoo(AbstractTela):
    def __init__(self):
        super().__init__(
            {
                1: "Incluir Voo",
                2: "Alterar Voo",
                3: "Listar Voos",
                4: "Excluir Voo",
                0: "Voltar",
            }
        )

    def tela_opcoes(self):
        print("-------- Voos ----------")
        for index, opcao in self.opcoes.items():
            print(f"{index} - {opcao}")

        return self.verifica_opcao("Escolha uma opção: ")

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
                verifica_data(data_do_voo)
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
                verifica_data(data_do_voo)
                break

            except Exception:
                print("Dado invalido, digite novamente!!!")

        return {
            "partida": partida,
            "destino": destino,
            "data_do_voo": data_do_voo,
        }

    def mostra_voo(self, dados_voo: dict):
        for chave, valor in dados_voo.items():
            print(f"{chave}: {valor}")

        print("\n")

    def seleciona_voo(self):
        codigo = input("Insira o código do voo que deseja selecionar: ").upper()
        return codigo
