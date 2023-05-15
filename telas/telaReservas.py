import string
from typing import TypedDict
from telas.abstractTela import AbstractTela
from entidades.voo import Voo


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

    def mostra_opcoes(self):
        print("-------- Reservas ----------")

        for index, opcao in self.opcoes.items():
            print(f"{index} - {opcao}")

        return self.verifica_opcao("Escolha uma opção: ")

    def pega_cpf(self, alterando=False):
        while True:
            try:
                cpf = input("Digite o CPF do passageiro: ").strip()

                if not cpf and alterando:
                    return cpf

                self.verica_cpf(cpf)
                return cpf

            except Exception as e:
                print(str(e))

    def verica_cpf(self, cpf):
        if not cpf.isdigit():
            raise Exception("O CPF deve ser composto por dígitos!")

    def pega_voo(self):
        while True:
            codigo_voo = input("Digite o código do Voo: ").upper().strip()

            if codigo_voo:
                return codigo_voo

            else:
                print("Dado invalido, digite novamente!!!")

    def pega_fileira(self, alterando=False):
        while True:
            try:
                fileira = input("Digite o número da fileira desejada: ").strip()

                if not fileira and alterando:
                    return 0

                if not fileira:
                    raise Exception("O campo nao pode ser vazio!")

                if not fileira.isdigit():
                    raise Exception("A fileira deve ser composta por números!")

                if int(fileira) < 1:
                    raise Exception("A fileira deve ser maior que 1!")

                return int(fileira)

            except Exception as e:
                print(str(e))

    def pega_assento_fileira(self, alterando=False):
        while True:
            try:
                assento = input("Digite a letra do assento desejado: ").upper().strip()

                if not assento and alterando:
                    return ""

                if not assento:
                    raise Exception("O campo nao pode ser vazio!")

                if assento not in string.ascii_uppercase:
                    raise Exception("O campo assento deve ser uma letra!")

                return assento

            except Exception as e:
                print(str(e))

    def mostra_reserva(self, dados_reserva: "dict[str, str]"):
        for chave, valor in dados_reserva.items():
            print(f"{chave}: {valor}")

        print("\n")

    def mostra_assentos_voo(self, voo: Voo):
        print("{:<1} ".format(""), end="")

        for i in range(voo.aviao.assentos_por_fileira):
            print("[{:^1}] | ".format(string.ascii_uppercase[i]), end="")
        print()

        for i in range(voo.aviao.fileiras):
            print("{} ".format(i + 1), end="")

            for j in range(voo.aviao.assentos_por_fileira):
                print("[{:^1}] | ".format(voo.assentos[i][j]), end="")

            print()

    def seleciona_reserva(self) -> str:
        codigo_reserva = (
            input("Insira o código da reserva que deseja buscar: ").upper().strip()
        )

        return codigo_reserva
