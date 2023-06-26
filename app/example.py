from customtkinter import CTkLabel, CTkButton

from telas.abstractFrame import AbstractFrame
from controladores.abstractControlador import AbstractController, AbstractControllerSet

from app import App


class TelaSistema(AbstractFrame):
    def _init_components(self):
        self.configurar_grid(self, row=0, column=0)

        CTkLabel(master=self, text="Tela Sistema").pack(pady=12, padx=10)
        for opcao in [1, 2, 3]:
            CTkButton(
                master=self,
                text=f"Botao{opcao}",
                command=lambda opcao=opcao: self.seleciona_opcao(opcao),
            ).pack(pady=12, padx=10)

    def seleciona_opcao(self, opcao: int):
        if self.controller:
            self.controller.seleciona_opcao(opcao)


class TelaVoo(AbstractFrame):
    def _init_components(self):
        self.configurar_grid(self, row=0, column=0)

        CTkLabel(master=self, text="Tela Voo").pack(pady=12, padx=10)
        for opcao in [1, 2, 3]:
            CTkButton(
                master=self,
                text=f"TelaVoo{opcao}",
                command=lambda opcao=opcao: self.seleciona_opcao(opcao),
            ).pack(pady=12, padx=10)

    def seleciona_opcao(self, opcao: int):
        if self.controller:
            self.controller.seleciona_opcao(opcao)


class ControladorVoo(AbstractController):
    VIEW_CLASS = TelaVoo

    def seleciona_opcao(self, opcao):
        self.parent.get_controlador("main").view.show()


class ControladorSistema(AbstractControllerSet):
    VIEW_CLASS = TelaSistema

    def seleciona_opcao(self, opcao):
        self.get_controlador("voo").start()


class AppSistemaExemplo(App):
    def _init_config(self):
        controlador_sistema = ControladorSistema(self)
        controlador_sistema.add_controlador("voo", ControladorVoo(self))

        self.add_controlador("main", controlador_sistema)

    @property
    def main(self):
        return self.get_controlador("main")

    def _start(self):
        self.main.start()
