from controladores.controladorSistema import ControladorSistema
from telas.telaSistema import TelaSistema
from telas.telaReservas import TelaReservas


class ControladorReservas:
    def __init__(self, controlador_sistema: ControladorSistema):
        self.__tela_reservas = TelaReservas()
        self.__controlador_sistema = controlador_sistema
        self.__reservas = []

    @property
    def reservas(self):
        return self.__reservas

    def incluir_reserva(self):
        pass

    def alterar_reserva(self):
        pass

    def excluir_reserva(self):
        pass

    def listar_reservas(self):
        pass

    def buscar_reserva_por_codigo(self, codigo):
        pass

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes_controlador = {
            1: self.incluir_reserva,
            2: self.alterar_reserva,
            3: self.excluir_reserva,
            4: self.listar_reservas,
            0: self.retornar,
        }

        while True:
            opcao_escolhida = self.__tela_reservas.mostra_opcoes()

            opcoes_controlador[opcao_escolhida]()
