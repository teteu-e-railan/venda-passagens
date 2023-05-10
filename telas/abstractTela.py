from abc import ABC


class AbstractTela(ABC):
    def verifica_opcao(mensagem: str, opcoes_validas: list[int]):
        while True:
            opcao_selecionada = int(input(mensagem))

            try:
                if opcao_selecionada not in opcoes_validas:
                    raise ValueError

                return opcao_selecionada

            except ValueError:
                print("Valor incorreto: Digite um valor válido!")
                print("Opções válidas:", opcoes_validas)

    def mostra_mensagem(mensagem: int):
        print(mensagem)
