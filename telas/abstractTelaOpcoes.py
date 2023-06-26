from customtkinter import CTkLabel, CTkButton
from telas.abstractFrame import AbstractFrame


class AbstractTelaOpcoes(AbstractFrame):
    def __init__(self, parent, controller, opcoes: "dict[int, str]"):
        super().__init__(parent, controller)

        self.__opcoes = opcoes

    @property
    def opcoes(self):
        return self.__opcoes

    def _init_components(self):
        self.configurar_grid(self, row=0, column=0)

        CTkLabel(master=self, text="Tela Sistema").pack(pady=12, padx=10)
        for index, opcao in self.opcoes.items():
            CTkButton(
                master=self,
                text=opcao,
                command=lambda index=index: self.controller.seleciona_opcao(index),
            ).pack(pady=12, padx=10)
