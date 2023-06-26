from controladores.abstractControlador import AbstractControllerSet
from telas.telaSistema import TelaSistema
from controladores.controladorReservas import ControladorReservas
from controladores.controladorAviao import ControladorAviao
from controladores.controladorPassageiro import ControladorPassageiro
from controladores.controladorTripulante import ControladorTripulante
from controladores.controladorVoo import ControladorVoo


class ControladorSistema(AbstractControllerSet):
    VIEW_CLASS = TelaSistema

    def __init__(self, parent):
        super().__init__(parent)

        # TODO add controladores `self.add_controlador()`
        # self.__controladores = {
        #     1: self.controlador_reservas.abre_tela,
        #     2: self.controlador_passageiros.abre_tela,
        #     3: self.controlador_tripulantes.abre_tela,
        #     4: self.controlador_voos.abre_tela,
        #     5: self.controlador_avioes.abre_tela,
        #     0: self.finaliza_sistema,
        # }

        self.__controlador_reservas = ControladorReservas(self.parent)
        self.__controlador_passageiros = ControladorPassageiro(self)
        self.__controlador_tripulantes = ControladorTripulante(self)
        self.__controlador_voos = ControladorVoo(self)
        self.__controlador_avioes = ControladorAviao(self)

    @property
    def controlador_reservas(self) -> ControladorReservas:
        return self.__controlador_reservas

    @property
    def controlador_passageiros(self) -> ControladorPassageiro:
        return self.__controlador_passageiros

    @property
    def controlador_tripulantes(self) -> ControladorTripulante:
        return self.__controlador_tripulantes

    @property
    def controlador_voos(self) -> ControladorVoo:
        return self.__controlador_voos

    @property
    def controlador_avioes(self) -> ControladorAviao:
        return self.__controlador_avioes

    # def inicializa_sistema(self):
    #     self.abre_tela()

    def finaliza_sistema(self):
        self.parent.stop()
        exit(0)

    def seleciona_opcao(self, index: int):
        opcoes_controlador = {
            1: self.controlador_reservas.start,
            2: self.controlador_passageiros.abre_tela,
            3: self.controlador_tripulantes.abre_tela,
            4: self.controlador_voos.abre_tela,
            5: self.controlador_avioes.abre_tela,
            0: self.finaliza_sistema,
        }

        opcoes_controlador[index]()

    # def abre_tela(self):
    #     opcoes_controlador = {
    #         1: self.controlador_reservas.abre_tela,
    #         2: self.controlador_passageiros.abre_tela,
    #         3: self.controlador_tripulantes.abre_tela,
    #         4: self.controlador_voos.abre_tela,
    #         5: self.controlador_avioes.abre_tela,
    #         0: self.finaliza_sistema,
    #     }

    #     while True:
    #         opcao_escolhida = self.__tela_sistema.mostra_opcoes()
    #         opcoes_controlador[opcao_escolhida]()
