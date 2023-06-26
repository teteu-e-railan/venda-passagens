from abc import ABC, abstractmethod
import customtkinter


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
    
    def centralizar_janela(self, nova_janela, altura: int, lagura: int):
        # Definir a largura e altura desejadas da janela
        largura_janela = lagura
        altura_janela = altura
        
        # Obter a largura e altura da tela
        largura_tela = nova_janela.winfo_screenwidth()
        altura_tela = nova_janela.winfo_screenheight()
        
        # Calcular as coordenadas para centralizar a janela
        x = (largura_tela - largura_janela) // 2
        y = (altura_tela - altura_janela) // 2
        
        # Definir a geometria da janela para centralizá-la
        return f"{largura_janela}x{altura_janela}+{x}+{y}"

    def verifica_opcao(self, mensagem: str) -> int:
        """Verifica a opção digitada e a retorna.

        Este método recebe um input e verifica-o para saber se é uma opção válida,
        de acordo com a lista de opções válidas. Caso seja uma opção válida,
        retorna a opção selecionada, senão é lançado um erro e novamente
        tenta-se receber um input.
        """
        while True:
            try:
                opcao_selecionada = int(input(mensagem))
                if opcao_selecionada not in self.lista_de_opcoes_validas:
                    raise ValueError

                return opcao_selecionada

            except ValueError:
                print("Valor incorreto: Digite um valor válido!")
                print("Opções válidas:", self.lista_de_opcoes_validas)

    def mostra_mensagem(self, mensagem: str):
        # Configurações da interface gráfica
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('green')

        # Criar uma nova janela
        nova_janela = customtkinter.CTk()
        nova_janela.geometry(self.centralizar_janela(nova_janela, 200, 400))
        nova_janela.title("Mensagem")

        # Criar o frame principal
        frame_principal = customtkinter.CTkFrame(master=nova_janela, corner_radius=10, border_width=4, border_color='green')
        frame_principal.pack(pady=80, padx=40, side='top', fill='both', expand=True)

        # Label para a mensagem
        label_mensagem = customtkinter.CTkLabel(master=frame_principal, text=mensagem, font=('Tahoma', 12))
        label_mensagem.pack(pady=10)

        # Definir função para fechar a janela após 4 segundos
        def fechar_janela():
            nova_janela.destroy()

        nova_janela.after(1000, fechar_janela)
        nova_janela.mainloop()


    def confirma_opcao(self, mensagem: str) -> bool:
        # Configurações da interface gráficaSs
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('green')
        escolha = None
        # Criar uma nova janela
        nova_janela = customtkinter.CTk()
        nova_janela.geometry(self.centralizar_janela(nova_janela, 200, 500))
        nova_janela.title("Confirmação")

        def sim():
            nonlocal escolha
            escolha = True
            nova_janela.destroy()

        def nao():
            nonlocal escolha
            escolha = False
            nova_janela.destroy()

        label = customtkinter.CTkLabel(nova_janela, text=mensagem, font=('Tahoma', 24))
        label.pack(pady=12, padx=10)

        botão_sim = customtkinter.CTkButton(nova_janela, text="Sim", command=sim)
        botão_sim.pack(side="bottom", pady=12, padx=10)
        botão_nao = customtkinter.CTkButton(nova_janela, text="Não", command=nao)
        botão_nao.pack(side="bottom", pady=12, padx=40)

        nova_janela.mainloop()
        return escolha