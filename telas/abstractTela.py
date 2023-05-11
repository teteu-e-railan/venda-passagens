from abc import ABC, abstractmethod


class AbstractTela(ABC):
    @abstractmethod
    def __init__(self, opcoes: "dict[int, str]"):
        self.__opcoes = opcoes
        self.__lista_de_opcoes_validas = list(opcoes.keys())

    @property
    def opcoes(self):
        return self.__opcoes

    @property
    def lista_de_opcoes_validas(self):
        return self.__lista_de_opcoes_validas

    def verifica_opcao(self, mensagem: str) -> int:
        while True:
            opcao_selecionada = int(input(mensagem))

            try:
                if opcao_selecionada not in self.lista_de_opcoes_validas:
                    raise ValueError

                return opcao_selecionada

            except ValueError:
                print("Valor incorreto: Digite um valor válido!")
                print("Opções válidas:", self.lista_de_opcoes_validas)

    def mostra_mensagem(self, mensagem: int):
        print(mensagem)
