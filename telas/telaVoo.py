from typing import TypedDict, Optional
from telas.abstractTela import AbstractTela


class DadosVoo(TypedDict):
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

    def pega_dados_voo(self, novo_voo=True) -> DadosVoo:
        print("-------- DADOS VOO ----------")
        partida = input("Local de partida do Voo: ").upper()
        destino = input("Local de destino do Voo: ").upper()
        data_do_voo = input("Data do Voo (formato: DD/MM/AAAA): ")
        modelo_aviao = input("Modelo do Avião que realizará o Voo: ").upper()

        return {
            "partida": partida,
            "destino": destino,
            "data_do_voo": data_do_voo,
            "modelo_aviao": modelo_aviao,
        }

    def pega_dados_altera_voo(self) -> DadosAlteraVoo:
        print("-------- DADOS VOO ----------")
        partida = input("Local de partida do Voo: ").upper()
        destino = input("Local de destino do Voo: ").upper()
        data_do_voo = input("Data do Voo (formato: DD/MM/AAAA): ")

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
