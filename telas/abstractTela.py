from abc import ABC, abstractmethod


class AbstractTela(ABC):
    """Tela Abstrata que fornece funcionalidades comuns a todas as telas do sistema.

    Exemplo de uso:
        class Tela(AbstractTela):
            def __init__(self):
                super().__init__({ 1: "Opcao 1", 2: "Opcao 2", ... })
    """

    @abstractmethod
    def __init__(self, opcoes: "dict[int, str]"):
        self.__opcoes = opcoes
        self.__lista_de_opcoes_validas = list(opcoes.keys())

    @property
    def opcoes(self):
        return self.__opcoes

    @property
    def lista_de_opcoes_validas(self):
        """
        Retorna uma lista de opcoes validas a partir
        das chaves do dicionário de opcoes.
        """
        return self.__lista_de_opcoes_validas

    def verifica_opcao(self, mensagem: str) -> int:
        """Verifica a opção digitada e a retorna.

        Este método recebe um input e verifica-o para saber se é uma opção válida,
        de acordo com a lista de opções válidas. Caso seja uma opção válida,
        retorna a opção selecionada, senão é lançado um erro e novamente
        tenta-se receber um input.
        """
        while True:
            opcao_selecionada = int(input(mensagem))

            try:
                if opcao_selecionada not in self.lista_de_opcoes_validas:
                    raise ValueError

                return opcao_selecionada

            except ValueError:
                print("Valor incorreto: Digite um valor válido!")
                print("Opções válidas:", self.lista_de_opcoes_validas)

    def mostra_mensagem(self, mensagem: str):
        """Mostra uma mensagem qualquer."""
        print(mensagem)
